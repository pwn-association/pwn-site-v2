# Generated by Django 3.2.13 on 2022-05-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwn_event', '0005_auto_20220512_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='link',
        ),
        migrations.AddField(
            model_name='speaker',
            name='url',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='external link'),
        ),
    ]
