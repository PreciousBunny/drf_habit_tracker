from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone',
                  'city', 'role',)


class ForCreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
