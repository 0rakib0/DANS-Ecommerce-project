# Generated by Django 3.2.19 on 2023-08-22 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Width',
        ),
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='lenth',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_meterials',
        ),
    ]
