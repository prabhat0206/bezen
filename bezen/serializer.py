from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Record
from django.contrib.auth.models import User

class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
