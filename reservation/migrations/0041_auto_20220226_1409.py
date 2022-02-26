# Generated by Django 3.2 on 2022-02-26 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0040_auto_20220226_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
