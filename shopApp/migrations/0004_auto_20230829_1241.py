# Generated by Django 3.2.19 on 2023-08-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_auto_20230829_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product-color-image')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_color_image',
        ),
        migrations.AddField(
            model_name='product',
            name='product_color_image',
            field=models.ManyToManyField(blank=True, null=True, to='shopApp.ColorImage'),
        ),
    ]
