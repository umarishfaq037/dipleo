from rest_framework import serializers
from .models import Company, Users, Jobs


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Jobs
        fields = '__all__'
