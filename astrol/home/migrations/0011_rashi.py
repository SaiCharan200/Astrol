# Generated by Django 4.1.3 on 2022-12-03 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_traits_negative_alter_traits_positive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rashi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nakshatra', models.CharField(default='', max_length=20)),
                ('rashi', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
