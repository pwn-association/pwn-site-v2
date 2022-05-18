# Generated by Django 3.2.13 on 2022-05-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwn_event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='country',
        ),
        migrations.AddField(
            model_name='place',
            name='address2',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='address complement'),
        ),
    ]
