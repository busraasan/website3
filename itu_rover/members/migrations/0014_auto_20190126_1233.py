# Generated by Django 2.0.1 on 2019-01-26 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_technicalteamleader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicalteamleader',
            name='member',
        ),
        migrations.DeleteModel(
            name='TechnicalTeamLeader',
        ),
    ]
