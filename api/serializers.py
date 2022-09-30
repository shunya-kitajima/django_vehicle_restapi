from rest_framework import serializers
from django.contrib.auth.models import User
from models import Segment, Brand, Vehicle


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True, "min_length": 5}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user


