# Generated by Django 3.2.21 on 2023-09-06 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0007_banner1_banner2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availableSize',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
