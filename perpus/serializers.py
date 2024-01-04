from rest_framework import serializers
from .models import Anggota

class Serial_Register(serializers.ModelSerializer):
  class Meta:
    model = Anggota
    fields = [
      'nama', 'jenis_kelamin', 'alamat', 'email', 'telepon', 'password'
    ]

class Serial_Login(serializers.ModelSerializer):
  class Meta:
    model = Anggota
    fields = [
      'email', 'password'
    ]