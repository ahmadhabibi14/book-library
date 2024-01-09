from rest_framework import serializers
from .models import User

class Serial_Register(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'nama', 'jenis_kelamin', 'alamat', 'email', 'telepon', 'password'
    ]

class Serial_Login(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'email', 'password'
    ]

class Serial_ID(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'id'
    ]