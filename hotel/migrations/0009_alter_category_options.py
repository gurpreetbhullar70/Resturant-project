# Generated by Django 3.2 on 2022-01-27 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
