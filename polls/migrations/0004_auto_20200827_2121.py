# Generated by Django 3.0.3 on 2020-08-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200827_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='privkey',
            field=models.CharField(default=False, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='pubkey',
            field=models.CharField(default=False, max_length=500),
        ),
    ]
