# Generated by Django 3.0.7 on 2020-08-01 22:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tramite', '0003_auto_20200801_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='tramite',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tramite',
            name='fecha_creado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tramite',
            name='fecha_modificado',
            field=models.DateField(auto_now=True),
        ),
    ]