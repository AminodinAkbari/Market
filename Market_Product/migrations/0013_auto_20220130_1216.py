# Generated by Django 3.2.11 on 2022-01-30 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Market_Product', '0012_auto_20220130_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='variants',
        ),
        migrations.DeleteModel(
            name='Variants',
        ),
    ]
