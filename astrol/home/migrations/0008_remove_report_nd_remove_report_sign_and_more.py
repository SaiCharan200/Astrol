# Generated by Django 4.1.3 on 2022-12-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='nd',
        ),
        migrations.RemoveField(
            model_name='report',
            name='sign',
        ),
        migrations.RemoveField(
            model_name='report',
            name='zsign',
        ),
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='firstname',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AddField(
            model_name='report',
            name='gender',
            field=models.CharField(default='null', max_length=1),
        ),
        migrations.AddField(
            model_name='report',
            name='lastname',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AddField(
            model_name='report',
            name='month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]