# Generated by Django 3.0.3 on 2020-09-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20200912_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='privkey',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pubkey',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
