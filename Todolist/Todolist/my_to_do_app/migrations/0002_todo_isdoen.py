# Generated by Django 4.0 on 2021-12-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isDoen',
            field=models.BooleanField(default=False),
        ),
    ]
