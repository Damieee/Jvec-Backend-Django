from rest_framework import serializers
from .models import MyCustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCustomUser
        fields = ['id', 'first_name', 'last_name', 'email']
