# Generated by Django 3.0.7 on 2020-06-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creado', models.DateField(auto_now_add=True)),
                ('fecha_modificado', models.DateField(auto_now=True)),
            ],
        ),
    ]
