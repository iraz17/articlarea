# Generated by Django 5.0.2 on 2024-02-24 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_category_articles_composition_articles_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(default='none', null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.category'),
        ),
    ]
