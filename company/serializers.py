from rest_framework import serializers
from .models import Company, Users


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'
