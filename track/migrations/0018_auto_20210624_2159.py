# Generated by Django 3.1.6 on 2021-06-24 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0017_auto_20210624_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='exercises',
        ),
        migrations.DeleteModel(
            name='Plans',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Exercises',
        ),
    ]