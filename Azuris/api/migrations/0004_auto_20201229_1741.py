# Generated by Django 3.1.4 on 2020-12-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobs',
            name='DMG',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mobs',
            name='HP',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobs',
            name='Level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobs',
            name='XP',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spells',
            name='Cooldown',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spells',
            name='Evasion_rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='spells',
            name='Level_requirement',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spells',
            name='Power',
            field=models.IntegerField(),
        ),
    ]