# Generated by Django 4.0.5 on 2022-07-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_cuisine_cuisine_alter_diet_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(max_length=800, verbose_name='instructions'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.FloatField(),
        ),
    ]
