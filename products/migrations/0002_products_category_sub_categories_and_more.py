# Generated by Django 4.1 on 2022-10-05 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
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
        migrations.AddField(
            model_name='products',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.sub_categories'),
        ),
    ]
