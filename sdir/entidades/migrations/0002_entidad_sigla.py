# Generated by Django 3.0.7 on 2020-08-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad',
            name='sigla',
            field=models.CharField(default=123456, max_length=6),
            preserve_default=False,
        ),
    ]