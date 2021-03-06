# Generated by Django 3.0.3 on 2020-10-06 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockapp', '0015_auto_20201006_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='next1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockapp.block'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
