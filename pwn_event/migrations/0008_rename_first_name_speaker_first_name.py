# Generated by Django 3.2.23 on 2023-11-23 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pwn_event', '0007_auto_20220518_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='first_Name',
            new_name='first_name',
        ),
    ]
