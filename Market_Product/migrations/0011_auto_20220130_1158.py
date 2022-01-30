# Generated by Django 3.2.11 on 2022-01-30 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Market_Product', '0010_alter_variants_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variants',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size and Color', 'Size and Color')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='variants',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Market_Product.product'),
        ),
    ]
