# Generated by Django 3.2 on 2022-02-25 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0027_customer_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='user',
            new_name='manger',
        ),
    ]