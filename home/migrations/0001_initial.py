# Generated by Django 4.0 on 2021-12-12 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='media')),
                ('url', models.URLField(blank=True)),
                ('rank', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('slug', models.CharField(max_length=400, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('logo', models.ImageField(upload_to='media')),
                ('address', models.TextField()),
                ('phone', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='media')),
                ('url', models.URLField(blank=True)),
                ('rank', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('slug', models.CharField(max_length=400, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('slug', models.CharField(max_length=400, unique=True)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('labels', models.CharField(blank=True, choices=[('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default')], max_length=400)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('inactive', 'inactive')], max_length=400)),
                ('stock', models.CharField(blank=True, choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=400)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
    ]
