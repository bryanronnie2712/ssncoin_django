# Generated by Django 3.0.3 on 2020-09-17 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockapp', '0007_auto_20200915_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
