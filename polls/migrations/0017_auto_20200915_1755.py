# Generated by Django 3.0.3 on 2020-09-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20200912_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='privkey',
            field=models.CharField(default=0, max_length=5000, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pubkey',
            field=models.CharField(default=0, max_length=5000, unique=True),
        ),
    ]
