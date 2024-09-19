# Generated by Django 4.2.16 on 2024-09-19 12:14

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):
    dependencies = [
        ("pwn_event", "0016_alter_event_description_alter_event_excerpt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="speaker",
            name="biography",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="biography"
            ),
        ),
    ]
