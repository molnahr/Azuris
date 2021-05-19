# Generated by Django 3.1.4 on 2020-12-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201229_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('data_joined', models.DateTimeField(auto_now_add=True, verbose_name='data joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('level', models.IntegerField(default=1)),
                ('xp', models.IntegerField(default=0)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Mobs',
        ),
        migrations.DeleteModel(
            name='Spells',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
