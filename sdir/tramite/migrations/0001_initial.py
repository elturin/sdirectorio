# Generated by Django 3.0.7 on 2020-08-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cut', models.CharField(max_length=10)),
                ('ruc', models.CharField(max_length=11)),
                ('fecha_creado', models.DateField(auto_now_add=True)),
                ('fecha_modificado', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cut', models.CharField(max_length=10)),
                ('ruc', models.CharField(max_length=11)),
                ('numero', models.IntegerField(max_length=50)),
                ('accion', models.CharField(max_length=300)),
                ('fecha_creado', models.DateField(auto_now_add=True)),
                ('fecha_modificado', models.DateField(auto_now=True)),
            ],
        ),
    ]
