# Generated by Django 4.1 on 2022-09-05 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cigarettes', '0009_alter_modelcart_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='modelcart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterModelOptions(
            name='modelproduct',
            options={'verbose_name': 'Каталог', 'verbose_name_plural': 'Каталог'},
        ),
        migrations.AlterField(
            model_name='modelproduct',
            name='brand',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='modelproduct',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='modelproduct',
            name='photo_url',
            field=models.ImageField(blank=True, default=None, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='modelproduct',
            name='price',
            field=models.IntegerField(default=None, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='modelproduct',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Cigarettes.modelcategory'),
        ),
    ]