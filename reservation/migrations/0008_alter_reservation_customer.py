# Generated by Django 3.2 on 2022-02-09 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_auto_20220208_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservation.table'),
        ),
    ]
