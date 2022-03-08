from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import fields, serializers, exceptions
from django.utils.translation import gettext_lazy as _
from django.urls import exceptions as url_exceptions
from project import settings

from .models import CustomUser

class CustomRegisterSerializer(RegisterSerializer):

    username = serializers.CharField(
        required=settings.USERNAME_REQUIRED,
    )

class CustomLoginSerializer(LoginSerializer):
    pass
    
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CelerySerializer(serializers.Serializer):
    number = serializers.IntegerField()