from django.contrib.auth.hashers import check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from apps.account.models import Account


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        model = Account
        fields = ('full_name', 'email', 'password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': 'Password did not match, please try again'})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        email = obj.get('email')
        tokens = Account.objects.get(email=email).tokens
        return tokens

    class Meta:
        model = Account
        fields = ('email', 'tokens', 'password')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed({
                'message': 'Email or password is not correct'
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'message': 'Account disabled'
            })

        data = {
            'email': user.email,
        }
        return data


class EmailVerificationSerializer(serializers.ModelSerializer):
    tokens = serializers.CharField(max_length=555)

    class Meta:
        model = Account
        fields = ('tokens',)


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Account
        fields = ('email',)


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'full_name', 'image_url', 'email', 'phone',)


class AccountOwnImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('image',)


class SetNewPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=64, write_only=True)
    uidb64 = serializers.CharField(max_length=68, required=True)
    tokens = serializers.CharField(max_length=555, required=True)

    class Meta:
        model = Account
        fields = ('password', 'password2', 'uidb64', 'tokens')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        uidb64 = attrs.get('uidb64')
        tokens = attrs.get('tokens')
        _id = force_str(urlsafe_base64_decode(uidb64))
        user = Account.objects.filter(id=_id).first()
        current_password = user.password
        if not PasswordResetTokenGenerator().check_token(user, tokens):
            raise AuthenticationFailed({'success': False, 'message': 'The token is not valid'})
        if password != password2:
            raise serializers.ValidationError({
                'success': False, 'message': 'Password did not match, please try again'
            })

        if check_password(password, current_password):
            raise serializers.ValidationError(
                {'success': False, 'message': 'New password should not similar to current password'})

        user.set_password(password)
        user.save()
        return attrs
