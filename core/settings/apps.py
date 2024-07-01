# -*- coding: utf-8 -*-
from core.settings.base import *
from django.utils.translation import gettext_lazy as _


# ==============================================================================
# DJANGO CMS
# ==============================================================================
CMS_TEMPLATES = [
    ('standard.html', 'Page de contenu'),
    ('home.html', 'Page d\'accueil'),
    ('contact.html', 'Page de contact'),
    ('event_base.html', u'Page des évenement'),
]

CMS_SEO_FIELDS = True
CMS_PERMISSION = True

# ==============================================================================
# FILER
# ==============================================================================

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

FILER_IMAGE_USE_ICON = 32
FILER_IS_PUBLIC_DEFAULT = True
FILER_LINK_STYLES = (
    ("default", _("default")),
)
