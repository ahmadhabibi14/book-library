# Generated by Django 4.2.9 on 2024-01-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perpus', '0007_buku_deskripsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjaman',
            name='buku',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='perpus.buku'),
        ),
    ]
