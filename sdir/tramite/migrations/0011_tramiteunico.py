# Generated by Django 3.0.7 on 2020-08-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramite', '0010_auto_20200805_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='TramiteUnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('tramite', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_creado', models.DateField(auto_now_add=True)),
                ('fecha_modificado', models.DateField(auto_now=True)),
            ],
        ),
    ]
