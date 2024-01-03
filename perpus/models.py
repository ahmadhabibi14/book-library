from django.db import models

class kelamin(models.TextChoices):
  L = 'L', 'Laki-Laki'
  P = 'P', 'Perempuan'

class Anggota(models.Model):
  id = models.CharField(primary_key=True, max_length=36)
  nama = models.CharField(max_length=255)
  jenis_kelamin = models.CharField(max_length=1, choices=kelamin.choices, default=kelamin.L)
  alamat = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  telepon = models.CharField(max_length=16)
  password = models.CharField(max_length=255)

class Peminjaman(models.Model):
  id = models.CharField(primary_key=True, max_length=36)
  tgl_pinjam = models.DateField()
  tgl_kembali = models.DateField()
  anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)