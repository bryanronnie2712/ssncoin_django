# Generated by Django 3.0.3 on 2020-08-28 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20200828_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='privkey',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pubkey',
        ),
    ]
