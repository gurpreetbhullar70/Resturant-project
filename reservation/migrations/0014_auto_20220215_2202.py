# Generated by Django 3.2 on 2022-02-15 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0013_auto_20220215_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='reservation.customer'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table_booked', to='reservation.table'),
        ),
    ]
