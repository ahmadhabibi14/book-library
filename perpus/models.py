from django.db import models

class kelamin(models.TextChoices):
  L = 'L', 'Laki-Laki'
  P = 'P', 'Perempuan'

class Anggota(models.Model):
  id = models.CharField(primary_key=True, max_length=36)
  nama = models.CharField(max_length=255)
  jenis_kelamin = models.CharField(max_length=1, choices=kelamin.choices, default=kelamin.L)
  alamat = models.CharField(max_length=255)
  email = models.CharField(max_length=255, unique=True)
  telepon = models.CharField(max_length=16)
  password = models.CharField(max_length=255)

class Peminjaman(models.Model):
  id = models.CharField(primary_key=True, max_length=36)
  tgl_pinjam = models.DateTimeField()
  tgl_kembali = models.DateTimeField()
  anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)

class Penerbit(models.Model):
  id = models.CharField(primary_key=True, max_length=36)
  nama = models.CharField(max_length=255)

class Penulis(models.Model):
  id = models.CharField(primary_key=True, max_length=36)
  nama = models.CharField(max_length=255)

class Buku(models.Model):
  id = models.CharField(primary_key=True, max_length=36)
  judul = models.CharField(max_length=255)
  rilis = models.DateTimeField()
  penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE)
  penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE)