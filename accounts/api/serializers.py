from rest_framework import serializers
from accounts.models import User
from accounts.utils import code_generator

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser','is_admin', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Registration model
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user