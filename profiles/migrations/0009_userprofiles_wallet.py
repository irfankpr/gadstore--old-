# Generated by Django 4.1 on 2022-10-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_userprofiles_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='wallet',
            field=models.FloatField(null=True),
        ),
    ]