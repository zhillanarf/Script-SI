# Generated by Django 5.1.1 on 2024-10-22 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idePenelitian', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KataKunci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('jenis', models.CharField(max_length=1)),
                ('kategori', models.CharField(max_length=1)),
            ],
        ),
    ]
