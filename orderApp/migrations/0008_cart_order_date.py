# Generated by Django 3.2.21 on 2023-09-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0007_alter_order_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_date',
            field=models.DateField(auto_now=True),
        ),
    ]