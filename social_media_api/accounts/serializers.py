from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =  ['username', 'email', 'bio', 'profile_picture', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
	
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
        	username = validated_data['username'],
        	email = validated_data['email'],
        	password = validated_data['password'],
        	bio = validated_data.get('bio', ''),
        	profile_picture = validated_data.get('profile_picture'),
        )
        Token.objects.create(user=user)
        return user