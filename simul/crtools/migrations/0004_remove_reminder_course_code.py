# Generated by Django 2.1.7 on 2019-03-04 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crtools', '0003_auto_20190305_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='course_code',
        ),
    ]
