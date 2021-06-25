# Generated by Django 3.1.6 on 2021-06-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0019_day_exercises_plans'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Plans',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='exercise_done',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='exercise_unit',
        ),
        migrations.AddField(
            model_name='exercises',
            name='exercise_time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='fri',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='mon',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='sat',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='sun',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='thu',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='tue',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='wed',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='creator_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='exercise_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
