# Generated by Django 2.1.7 on 2019-03-04 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crtools', '0002_ttchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
