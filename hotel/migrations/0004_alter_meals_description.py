# Generated by Django 3.2 on 2022-01-26 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_meals_preparation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]