# Generated by Django 4.2.3 on 2023-07-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='des',
            field=models.CharField(default='exit', max_length=200),
            preserve_default=False,
        ),
    ]