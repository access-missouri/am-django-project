#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
"""
am URL Configuration.
"""

from django.conf.urls import url, include
from django.contrib import admin
from general.views import PersonDetailView, PersonVotesListView
from legislative.views import BillDetailView, VoteDetailView, BillVotesListView, BillTextDetailView
from django.conf.urls.static import static
from django.conf import settings

from search.views import BillSearchListView

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^bills/(?P<id>[\w-]+)/$', BillDetailView.as_view(), name='bill'),
                  url(r'^bills/(?P<id>[\w-]+)/votes/$', BillVotesListView.as_view(), name='billvotes'),
                  url(r'^bills/(?P<bill_id>[\w-]+)/votes/(?P<id>[\w-]+)/$', VoteDetailView.as_view(), name='vote'),
                  url(r'^bills/(?P<bill_id>[\w-]+)/text/(?P<id>[\w-]+)/$', BillTextDetailView.as_view(), name='billtext'),
                  url(r'^people/(?P<id>[\w-]+)/$', PersonDetailView.as_view(), name='person'),
                  url(r'^people/(?P<id>[\w-]+)/votes/$', PersonVotesListView.as_view(), name='personvotes'),
                  url(r'^search/bills/', BillSearchListView.as_view(), name='bill-search'),
                  url(r'^api/', include('api.urls', namespace='api')),
                  url(r'^finance/', include('finance.urls', namespace='finance')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
