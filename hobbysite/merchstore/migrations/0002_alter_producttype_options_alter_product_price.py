# Generated by Django 5.0.3 on 2024-03-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'ordering': ['name'], 'verbose_name': 'Product Type', 'verbose_name_plural': 'Product Types'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
