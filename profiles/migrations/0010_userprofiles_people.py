# Generated by Django 4.1 on 2022-10-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_userprofiles_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='people',
            field=models.IntegerField(default=0),
        ),
    ]
