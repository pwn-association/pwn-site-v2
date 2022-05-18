# Generated by Django 3.2.13 on 2022-05-11 13:34

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from=['name'], unique=True, verbose_name='slug')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
                'get_latest_by': '-start_date',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=250, unique=True, verbose_name='name')),
                ('first_Name', models.CharField(max_length=250, unique=True, verbose_name='name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from=['last_name', 'first_Name'], unique=True, verbose_name='slug')),
                ('biography', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='biography')),
                ('link', models.URLField(blank=True, max_length=250, null=True, verbose_name='url')),
                ('image', filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='image')),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from=['name'], unique=True, verbose_name='slug')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='biography')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='address')),
                ('town', models.CharField(blank=True, max_length=250, null=True, verbose_name='town')),
                ('zip', models.CharField(blank=True, max_length=250, null=True, verbose_name='zip')),
                ('country', models.CharField(blank=True, max_length=250, null=True, verbose_name='country')),
                ('link', models.URLField(blank=True, max_length=250, null=True, verbose_name='url')),
                ('image', filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='image')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from=['title'], unique=True, verbose_name='slug')),
                ('excerpt', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='excerpt')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('date', models.DateTimeField(verbose_name='Event date')),
                ('is_publish', models.BooleanField(default=True, verbose_name='is publish')),
                ('start_publication', models.DateTimeField(blank=True, help_text='Start date of publication.', null=True, verbose_name='start publication')),
                ('end_publication', models.DateTimeField(blank=True, help_text='End date of publication.', null=True, verbose_name='end publication')),
                ('image', filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='image')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pwn_event.place', verbose_name='place')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pwn_event.season', verbose_name='season')),
                ('speaker', models.ManyToManyField(to='pwn_event.Speaker')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'get_latest_by': '-date',
            },
        ),
    ]
