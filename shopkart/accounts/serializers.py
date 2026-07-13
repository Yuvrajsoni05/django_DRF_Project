from rest_framework import serializers
from .models import UserDetail
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = UserDetail
        fields = ['id', 'username','first_name', 'last_name', 'email', 'phone_number', 'password', 'role' , 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
        
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": " Password fields didn't match."})
        
    
        if UserDetail.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Email is already in use."})
        
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user = UserDetail.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        
        
        
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError({
    "detail": "Invalid username or password."
})
        else:
            raise serializers.ValidationError("Both username and password are required.")
        
        data['user'] = user
        return data




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'profile_picture']
        
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'profile_picture']
