# Generated by Django 3.1.4 on 2020-12-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_mob_spell'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='file_name',
        ),
        migrations.AddField(
            model_name='spell',
            name='file',
            field=models.TextField(default=1),
        ),
    ]
