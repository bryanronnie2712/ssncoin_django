# Generated by Django 3.0.3 on 2020-09-18 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20200918_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='achievements',
        ),
    ]
