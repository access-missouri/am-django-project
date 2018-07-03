#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Warn users if the server is showing data from a local database.
"""

from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('general/components/local_db_warning.html', takes_context=True)
def local_db_warning(context):
    try:
        local_db = True if settings.LOCAL_DB == True else False
    except (AttributeError):
        return {}
    return {
        'local_db': local_db,
    }
