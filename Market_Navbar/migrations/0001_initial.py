# Generated by Django 4.0 on 2021-12-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='نام آیتم منو')),
                ('url_name', models.CharField(max_length=100, verbose_name='آدرس در نوار آدرس')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات این آیتم')),
            ],
        ),
    ]
