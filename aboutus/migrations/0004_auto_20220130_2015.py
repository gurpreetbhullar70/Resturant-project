# Generated by Django 3.2 on 2022-01-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0003_auto_20220130_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='why_choose_us',
            name='heading',
            field=models.CharField(default='Why Us', max_length=30),
        ),
        migrations.AlterField(
            model_name='why_choose_us',
            name='paragrapgH',
            field=models.CharField(default='Why Choose Our Restaurant', max_length=50),
        ),
    ]
