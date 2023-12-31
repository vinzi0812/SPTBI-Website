# Generated by Django 4.1.6 on 2023-07-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/assets/cards')),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='incubatee',
            options={},
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='password',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='incubatee',
            name='username',
        ),
    ]
