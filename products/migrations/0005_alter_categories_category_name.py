# Generated by Django 4.1 on 2022-10-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]