# Generated by Django 3.1.6 on 2021-06-13 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_auto_20210613_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercises',
            name='fri',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='mon',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='plan_name',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='sat',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='sun',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='thu',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='tue',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='wed',
        ),
    ]
