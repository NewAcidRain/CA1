# Generated by Django 4.0.6 on 2022-07-27 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cigarettes', '0007_rename_product_modelcart_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelcart',
            old_name='product_id',
            new_name='product',
        ),
    ]