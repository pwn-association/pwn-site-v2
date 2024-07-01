# -*- coding: utf-8 -*-
""" Event model for Creation """

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from django_extensions.db.fields import AutoSlugField


class Season(models.Model):
    """ """
    name = models.CharField(_('name'), max_length=250, unique=True)
    slug = AutoSlugField(_('slug'), max_length=255, populate_from=['name'], unique=True, db_index=True)
    start_date = models.DateField(_('start date'),)
    end_date = models.DateField(_('end date'),)

    class Meta:
        get_latest_by = '-start_date'
        verbose_name = _('Season')
        verbose_name_plural = _('Seasons')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Builds and returns the category's URL
        based on his tree path.
        """
        return reverse('pwn_event:season_detail', kwargs={'slug': self.slug})
