# Generated by Django 4.1 on 2022-09-06 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cigarettes', '0017_rename_category_name_modelcategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelproduct',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cigarettes.modelcategory', verbose_name='Категория'),
        ),
    ]