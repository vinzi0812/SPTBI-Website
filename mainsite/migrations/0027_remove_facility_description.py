# Generated by Django 4.1.6 on 2023-07-26 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0026_facility_programme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='description',
        ),
    ]
