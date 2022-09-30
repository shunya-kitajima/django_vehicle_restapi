from rest_framework import serializers
from django.contrib.auth.models import User
from models import Segment, Brand, Vehicle


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True, "min_length": 5}}

