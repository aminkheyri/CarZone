# Generated by Django 3.2.3 on 2021-05-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_teams_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='facebook_link',
            field=models.URLField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]