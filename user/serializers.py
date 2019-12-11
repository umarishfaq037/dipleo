from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'