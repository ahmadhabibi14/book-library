from rest_framework import serializers
from .models import User, Buku

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


class Serial_Books(serializers.Serializer):
  judul = serializers.CharField()
  rilis = serializers.DateTimeField()
  thumbnail = serializers.CharField()
  penulis = serializers.CharField()