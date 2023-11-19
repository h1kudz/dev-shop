# Generated by Django 4.1.12 on 2023-11-16 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.FileField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Новая цена')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Старая цена')),
                ('is_available', models.BooleanField(default=True, verbose_name='В наличии')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добаления')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='products_ca_name_693421_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'slug'], name='products_pr_id_a08e3c_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='products_pr_name_9ff0a3_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-pub_date'], name='products_pr_pub_dat_b0d088_idx'),
        ),
    ]