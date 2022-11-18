from rest_framework import serializers
from apps.order.models import Order
from apps.account.api.v1.serializers import AccountSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = AccountSerializer()

    class Meta:
        model = Order
        fields = ("__all__")


    