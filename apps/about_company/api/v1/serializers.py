from rest_framework import serializers
from apps.about_company.models import AboutCompany


class AboutCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutCompany
        fields = '__all__'
