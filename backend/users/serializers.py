from rest_framework import serializers
from .models import User
from .encryption import encrypt_value, decrypt_value

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class ProfileSerializer(serializers.ModelSerializer):
    aadhaar = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'aadhaar']

    def update(self, instance, validated_data):
        aadhaar = validated_data.pop('aadhaar', None)
        if aadhaar:
            instance.aadhaar_encrypted = encrypt_value(aadhaar)
        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.aadhaar_encrypted:
            data['aadhaar'] = decrypt_value(instance.aadhaar_encrypted)
        return data