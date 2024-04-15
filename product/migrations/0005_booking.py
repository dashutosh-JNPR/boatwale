# Generated by Django 5.0.3 on 2024-04-15 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('contact_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('time_slot', models.TimeField(max_length=50)),
                ('pickup_ghat', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('route', models.CharField(max_length=200)),
                ('total_guests', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_id', models.CharField(max_length=50)),
                ('is_booked', models.BooleanField(default=False)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tour')),
            ],
        ),
    ]
