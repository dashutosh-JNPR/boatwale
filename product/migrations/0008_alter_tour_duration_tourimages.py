# Generated by Django 5.0.3 on 2024-04-01 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_boat_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='TourImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='tours/')),
                ('alt', models.CharField(blank=True, max_length=100, null=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tour')),
            ],
        ),
    ]