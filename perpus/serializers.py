from rest_framework import serializers
from .models import Anggota

class AnggotaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Anggota
    fields = [
      'nama', 'jenis_kelamin', 'alamat', 'email', 'telepon', 'password'
    ]