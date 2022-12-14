# Generated by Django 4.1 on 2022-10-29 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('category_image', models.ImageField(upload_to='products/category_images')),
            ],
        ),
        migrations.CreateModel(
            name='sub_categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_cat_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('parent_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories')),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=300, unique=True)),
                ('slug', models.SlugField()),
                ('products_desc', models.TextField()),
                ('products_dyl', models.TextField()),
                ('MRP', models.FloatField()),
                ('price', models.FloatField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='products/products_images')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('available_stock', models.BigIntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categories')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.sub_categories')),
            ],
        ),
        migrations.CreateModel(
            name='prodtct_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/products_images')),
                ('prodtct_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]
