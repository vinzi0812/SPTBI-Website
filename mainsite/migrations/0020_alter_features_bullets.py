# Generated by Django 4.1.6 on 2023-07-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0019_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='bullets',
            field=models.TextField(blank=True, null=True),
        ),
    ]
