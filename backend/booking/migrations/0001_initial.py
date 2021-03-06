# Generated by Django 2.0.2 on 2018-07-27 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0002_auto_20180726_1453'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField()),
                ('state', models.CharField(choices=[('booked', 'Booked'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('canceled', 'Canceled'), ('timeout', 'Timeout'), ('completed', 'completed')], default='Male', max_length=255)),
                ('review_mark', models.FloatField(blank=True, default=0.0)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone_number', models.CharField(max_length=50)),
                ('customer_email', models.CharField(max_length=50)),
                ('customer_description', models.TextField(blank=True)),
                ('customer_reminder', models.CharField(max_length=255)),
                ('customer_agree', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='bookings', to='service.Service')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
