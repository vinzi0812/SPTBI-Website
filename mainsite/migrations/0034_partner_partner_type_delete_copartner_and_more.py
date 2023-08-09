# Generated by Django 4.1.6 on 2023-08-01 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0033_stat_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/assets/partners')),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Partner_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('partners', models.ManyToManyField(to='mainsite.partner')),
            ],
        ),
        migrations.DeleteModel(
            name='CoPartner',
        ),
        migrations.DeleteModel(
            name='FundingPartner',
        ),
        migrations.DeleteModel(
            name='OurPartner',
        ),
    ]