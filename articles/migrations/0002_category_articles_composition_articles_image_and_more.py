# Generated by Django 5.0.2 on 2024-02-24 10:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='composition',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='articles_images/'),
        ),
        migrations.AddField(
            model_name='articles',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default=2, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.category'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('ordered', models.BooleanField(default=False)),
                ('ordered_date', models.DateTimeField(blank=True, null=True)),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('orders', models.ManyToManyField(to='articles.order')),
            ],
        ),
    ]