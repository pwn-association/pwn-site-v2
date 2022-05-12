# -*- coding: utf-8 -*-
""" Creation: Settings """

from django.conf import settings


PAGINATION = getattr(settings, 'PWN_EVENT_PAGINATION', 10)
