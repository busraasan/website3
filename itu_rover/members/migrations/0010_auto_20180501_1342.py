# Generated by Django 2.0.1 on 2018-05-01 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20180501_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamleader',
            name='leader',
        ),
        migrations.AddField(
            model_name='teamleader',
            name='member',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leader', to='members.Member', verbose_name='team leader'),
        ),
    ]