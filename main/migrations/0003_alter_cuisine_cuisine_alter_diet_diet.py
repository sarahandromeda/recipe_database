# Generated by Django 4.0.6 on 2022-07-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_difficulty_options_alter_cooktime_cook_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='cuisine',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='cuisine'),
        ),
        migrations.AlterField(
            model_name='diet',
            name='diet',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='diet'),
        ),
    ]
