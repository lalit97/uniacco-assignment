from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User Registration Serializer
    """
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User 
        fields = ('username', 'password')
    
    def validate_username(self, username):
        """
        Validate Username field
        """
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise serializers.ValidationError('Username already taken')
        return username 

    def create(self, validated_data):
        """
        Create New User
        """
        username = validated_data.get('username')
        password = validated_data.get('password')
        user = User.objects.create_user(username=username, password=password)
        return user
