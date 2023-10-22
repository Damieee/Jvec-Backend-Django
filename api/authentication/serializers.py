from rest_framework import serializers
from .models import MyCustomUser
import re
from email_validator import  validate_email, EmailNotValidError

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = MyCustomUser
        fields = ['first_name', 'username', 'last_name', 'email', 'password', 'confirm_password']

    def validate_email(self, value):
        # Validate email field
        if not value:
            raise serializers.ValidationError("Email is required.")
        try:
            v = validate_email(value)
            value = v["email"]
        except EmailNotValidError as e:
            raise serializers.ValidationError(str(e))
        if MyCustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_password(self, value):
        # Validate password field
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def validate(self, data):
        # Additional validation, e.g., confirm_password
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # Hash the password before saving to the database
        password = validated_data.pop('password')
        user = MyCustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
