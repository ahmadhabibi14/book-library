from django.db import models
import uuid
from datetime import datetime

class kelamin(models.TextChoices):
  L = 'L', 'Laki-Laki'
  P = 'P', 'Perempuan'

class User(models.Model):
  id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36)
  nama = models.CharField(max_length=100)
  jenis_kelamin = models.CharField(max_length=1, choices=kelamin.choices, default=kelamin.L)
  alamat = models.CharField(max_length=255)
  email = models.CharField(max_length=255, unique=True)
  telepon = models.CharField(max_length=16)
  password = models.CharField(max_length=255)
  petugas = models.BooleanField(default=False)
  join_at = models.DateTimeField(default=datetime.now())

class Penulis(models.Model):
  id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36)
  nama = models.CharField(max_length=255)

class Buku(models.Model):
  id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36)
  judul = models.CharField(max_length=255)
  rilis = models.DateTimeField(max_length=100)
  thumbnail = models.CharField(max_length=255, default='/media/books/default.png')
  slug = models.CharField(max_length=255, default='books', unique=True)
  deskripsi = models.TextField(default='Tidak ada deskripsi')
  penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE)

class Peminjaman(models.Model):
  id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36)
  tgl_pinjam = models.DateTimeField()
  tgl_kembali = models.DateTimeField()
  dikembalikan = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  buku = models.ForeignKey(Buku, on_delete=models.CASCADE, default=None)