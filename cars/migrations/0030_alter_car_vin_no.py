# Generated by Django 3.2.3 on 2021-05-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0029_auto_20210528_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin_no',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
