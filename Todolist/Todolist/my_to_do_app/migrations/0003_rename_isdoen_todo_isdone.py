# Generated by Django 4.0 on 2021-12-16 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0002_todo_isdoen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='isDoen',
            new_name='isDone',
        ),
    ]