# Generated by Django 3.0.5 on 2020-05-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_products', '0003_productdetail_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='subcategory',
            field=models.CharField(blank=True, db_index=True, max_length=120),
        ),
    ]