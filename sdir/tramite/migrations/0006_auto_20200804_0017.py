# Generated by Django 3.0.7 on 2020-08-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramite', '0005_auto_20200804_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tramite',
            name='cut',
            field=models.CharField(max_length=12),
        ),
    ]
