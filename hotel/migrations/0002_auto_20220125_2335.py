# Generated by Django 3.2 on 2022-01-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TimeField(max_length=500)),
                ('people', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, max_length=5)),
                ('preparation_time', models.Field()),
                ('image', models.ImageField(upload_to='hotel/')),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='table',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]