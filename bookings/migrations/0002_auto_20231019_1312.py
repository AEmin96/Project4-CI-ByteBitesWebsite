# Generated by Django 3.2.22 on 2023-10-19 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='password',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='repeat_email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='repeat_password',
        ),
    ]
