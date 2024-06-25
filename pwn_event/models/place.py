# -*- coding: utf-8 -*-
""" Event model for Creation """

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from django_extensions.db.fields import AutoSlugField
from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField


class Place(models.Model):
    """ """
    name = models.CharField(_('name'), max_length=250, unique=True)
    slug = AutoSlugField(_('slug'), max_length=255, populate_from=['name'], unique=True, db_index=True)
    image = FilerImageField(default=None, verbose_name=_("image"), null=True, blank=True, on_delete=models.SET_NULL)
    description = RichTextField(_('biography'), blank=True, null=True)
    address = models.CharField(_('address'), max_length=250, null=True, blank=True)
    address2 = models.CharField(_('address complement'), max_length=250, null=True, blank=True)
    zip = models.CharField(_('zip'), max_length=250, null=True, blank=True)
    city = models.CharField(_('city'), max_length=250, null=True, blank=True)
    url = models.URLField(_('external link'), max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_address(self):
        address_2 = ''
        if self.address2:
            address_2 = f" {self.address2}"
        return f"{self.name}, {self.address }{address_2}, {self.zip} {self.city}"

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

    def get_absolute_url(self):
        """
        Builds and returns the category's URL
        based on his tree path.
        """
        return reverse('pwn_event:place_detail', kwargs={'slug': self.slug})
