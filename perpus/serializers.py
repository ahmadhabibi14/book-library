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
  slug = serializers.CharField()
  penulis = serializers.CharField()

class Serial_Peminjaman(serializers.Serializer):
  id = serializers.CharField()
  buku = serializers.CharField()
  tgl_pinjam = serializers.DateTimeField()
  tgl_kembali = serializers.DateTimeField()
  slug = serializers.CharField()
  dikembalikan = serializers.BooleanField()

class Serial_Notifikasi(serializers.Serializer):
  id = serializers.CharField()
  pesan = serializers.CharField()
  tanggal = serializers.DateTimeField()
  dibaca = serializers.BooleanField()

class Serial_EditProfile(serializers.Serializer):
  nama = serializers.CharField()
  alamat = serializers.CharField()
  telepon = serializers.CharField()
  jenis_kelamin = serializers.CharField()