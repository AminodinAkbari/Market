# Generated by Django 4.0 on 2021-12-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market_Product', '0009_rename_name_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=100, unique=True),
        ),
    ]
