# Generated by Django 4.2.3 on 2023-07-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='des',
            field=models.CharField(default='', max_length=200),
        ),
    ]