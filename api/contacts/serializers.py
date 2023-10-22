from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'user']

    def validate_phone_number(self, value):
        """
        Custom validation for the phone_number field.
        Ensure that phone_number contains only digits and has a length of 10.
        """
        if not value.isdigit():
            raise serializers.ValidationError("Phone number should contain only digits.")
        if len(value) != 10:
            raise serializers.ValidationError("Phone number should have exactly 10 digits.")
        return value
