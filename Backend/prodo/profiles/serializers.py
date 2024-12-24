from rest_framework import serializers
from .models import AppUser
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    password_repeat = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = AppUser
        fields = ['email', 'password', 'password_repeat', 'birthdate', 'avatar']

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError("Passwords must match!")
        
        try:
            password_validation.validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})
        
        return data
    

    def create(self, validated_data):
        birthdate = validated_data.get('birthdate', None)
        avatar = validated_data.get('avatar', None)

        user = AppUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            birthdate = birthdate,
            avatar = avatar
        )

        return user