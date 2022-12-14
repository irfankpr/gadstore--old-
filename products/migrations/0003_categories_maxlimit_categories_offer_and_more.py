# Generated by Django 4.1 on 2022-10-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='maxlimit',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='categories',
            name='offer_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='offer_tittle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
