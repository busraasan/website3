# Generated by Django 2.0.1 on 2019-01-26 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_auto_20180501_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnicalTeamLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='techleader', to='members.Member', verbose_name='tech leader')),
            ],
            options={
                'verbose_name': 'tech leader',
                'verbose_name_plural': 'tech leader',
            },
        ),
    ]
