# Generated by Django 3.2 on 2022-02-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0009_alter_reservation_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
