# Generated by Django 5.0.3 on 2024-04-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_boat_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]