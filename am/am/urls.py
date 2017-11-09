#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
am URL Configuration.
"""

from django.conf.urls import url
from django.contrib import admin
from general.views import PersonDetailView
from legislative.views import BillDetailView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'bills/(?P<id>[\w-]+)/$', BillDetailView.as_view(), name='bill'),
                  url(r'people/(?P<id>[\w-]+)/$', PersonDetailView.as_view(), name='person'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
