# -*- coding: utf-8 -*-
""" Event model for Creation """

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from django_extensions.db.fields import AutoSlugField
from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField


class Speaker(models.Model):
    """ """
    last_name = models.CharField(_('last name'), max_length=250, unique=True)
    first_name = models.CharField(_('first name'), max_length=250, unique=True)
    slug = AutoSlugField(_('slug'), max_length=255, populate_from=['last_name', 'first_Name'], unique=True, db_index=True)
    image = FilerImageField(default=None, verbose_name=_("image"), null=True, blank=True, on_delete=models.SET_NULL)
    biography = RichTextField(_('biography'), blank=True, null=True)
    url = models.URLField(_('external link'), max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')

    def get_absolute_url(self):
        """
        Builds and returns the speaker's URL based on his detail path.
        """
        return reverse('pwn_event:speaker_detail', kwargs={'slug': self.slug})
