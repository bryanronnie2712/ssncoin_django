# Generated by Django 3.0.3 on 2020-10-06 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockapp', '0014_auto_20201001_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=40)),
                ('staff', models.CharField(max_length=40)),
                ('transaction', models.CharField(max_length=40)),
                ('proof', models.IntegerField(default=0)),
                ('department', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='block',
            name='next1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockapp.block'),
        ),
    ]
