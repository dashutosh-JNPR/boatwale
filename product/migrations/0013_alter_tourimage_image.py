# Generated by Django 5.0.3 on 2024-04-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_tour_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tours/'),
        ),
    ]