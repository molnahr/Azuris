# Generated by Django 3.1.4 on 2020-12-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20201230_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
