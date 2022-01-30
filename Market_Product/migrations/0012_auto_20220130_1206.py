# Generated by Django 3.2.11 on 2022-01-30 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Market_Product', '0011_auto_20220130_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Market_Product.color'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Market_Product.size'),
        ),
    ]
