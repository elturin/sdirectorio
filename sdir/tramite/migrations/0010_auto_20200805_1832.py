# Generated by Django 3.0.7 on 2020-08-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramite', '0009_auto_20200805_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tramite',
            name='paso',
            field=models.IntegerField(default=0),
        ),
    ]
