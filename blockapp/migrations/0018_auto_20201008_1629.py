# Generated by Django 3.0.3 on 2020-10-08 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockapp', '0017_auto_20201008_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='block',
            name='next1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockapp.block'),
        ),
    ]
