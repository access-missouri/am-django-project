#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
"""
am URL Configuration.
"""

from django.conf.urls import url
from django.contrib import admin
from general.views import PersonDetailView, PersonVotesListView
from legislative.views import BillDetailView, VoteDetailView, BillVotesListView
from django.conf.urls.static import static
from django.conf import settings

from search.views import BillSearchListView

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'bills/(?P<id>[\w-]+)/$', BillDetailView.as_view(), name='bill'),
                  url(r'bills/(?P<id>[\w-]+)/votes/$', BillVotesListView.as_view(), name='billvotes'),
                  url(r'bills/(?P<bill_id>[\w-]+)/votes/(?P<id>[\w-]+)/$', VoteDetailView.as_view(), name='vote'),
                  url(r'people/(?P<id>[\w-]+)/$', PersonDetailView.as_view(), name='person'),
                  url(r'people/(?P<id>[\w-]+)/votes/$', PersonVotesListView.as_view(), name='personvotes'),
                  url(r'^search/bills/', BillSearchListView.as_view(), name='bill-search'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
