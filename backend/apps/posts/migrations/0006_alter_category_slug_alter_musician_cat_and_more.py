# Generated by Django 4.1.7 on 2023-04-07 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_category_slug_musician_slug_alter_musician_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.category', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
