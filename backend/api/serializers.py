from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        # Create user with encrypted password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_name', 'author', 'author', 'created_at')
        extra_kwargs = {
            'id': {'read_only': True},
            'author': {'read_only': True}
        }