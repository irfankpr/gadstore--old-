# Generated by Django 4.1 on 2022-10-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]