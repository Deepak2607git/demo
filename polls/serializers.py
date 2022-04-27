from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .managers import CustomUserManager
from .models import Tutorial,User

class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


class UseSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


