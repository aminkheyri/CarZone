# Generated by Django 3.2.3 on 2021-05-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_car_passengers'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='vin_no',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(max_length=100),
        ),
    ]
