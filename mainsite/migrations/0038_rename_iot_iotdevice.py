# Generated by Django 4.1.6 on 2023-08-04 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0037_iot'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IoT',
            new_name='IotDevice',
        ),
    ]
