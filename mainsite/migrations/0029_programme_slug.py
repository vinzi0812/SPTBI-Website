# Generated by Django 4.1.6 on 2023-07-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0028_alter_programme_about_alter_programme_benefits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='slug',
            field=models.SlugField(default='nidhi-prayas', unique=True),
            preserve_default=False,
        ),
    ]