# Generated by Django 4.1 on 2022-10-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_category_sub_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
