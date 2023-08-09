# Generated by Django 4.1.6 on 2023-07-25 19:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0025_alter_incubatee_current_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/assets/facility')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('banner', models.ImageField(upload_to='static/assets/banner')),
                ('objectives', models.TextField()),
                ('broadcovered', models.TextField()),
                ('broadnotcovered', models.TextField()),
                ('eligible', models.TextField()),
                ('noteligible', models.TextField()),
                ('guidelines', models.TextField()),
                ('benefits', models.TextField()),
                ('facilities', models.ManyToManyField(to='mainsite.facility')),
                ('incubatees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]