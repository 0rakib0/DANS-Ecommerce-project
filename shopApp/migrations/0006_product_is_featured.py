# Generated by Django 3.2.19 on 2023-08-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0005_auto_20230829_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]