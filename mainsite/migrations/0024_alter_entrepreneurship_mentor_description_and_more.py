# Generated by Django 4.1.6 on 2023-07-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0023_alter_ipr_mentor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneurship_mentor',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='faculty_mentor',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='finance_mentor',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='marketing_mentor',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='sales_mentor',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='taxation_mentor',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]