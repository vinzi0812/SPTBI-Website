# Generated by Django 4.1.6 on 2023-07-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_cards_bullets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/assets/team')),
            ],
        ),
    ]