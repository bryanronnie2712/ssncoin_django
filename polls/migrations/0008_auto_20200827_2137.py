# Generated by Django 3.0.3 on 2020-08-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20200827_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='privkey',
            field=models.CharField(default='dfg', max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pubkey',
            field=models.CharField(default='abd', max_length=500, unique=True),
        ),
    ]
