# Generated by Django 3.0.7 on 2020-08-04 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramite', '0006_auto_20200804_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='cut',
            name='codtramite',
            field=models.CharField(default=123456789123, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cut',
            name='cut',
            field=models.CharField(max_length=12),
        ),
    ]