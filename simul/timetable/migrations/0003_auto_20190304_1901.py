# Generated by Django 2.1.7 on 2019-03-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20190304_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttformat',
            name='day',
            field=models.IntegerField(default=0),
        ),
    ]
