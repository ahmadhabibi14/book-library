# Generated by Django 4.2.9 on 2024-01-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpus', '0005_buku_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='slug',
            field=models.CharField(default='books', max_length=255, unique=True),
        ),
    ]