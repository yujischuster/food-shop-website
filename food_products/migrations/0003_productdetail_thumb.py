# Generated by Django 3.0.5 on 2020-05-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_products', '0002_productdetail_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
