from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book,AdminUser



class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = AdminUser
        fields = ['id', 'email', 'full_name', 'password']
    
    def create(self, validated_data):
        user = AdminUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data['full_name']
        )
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
