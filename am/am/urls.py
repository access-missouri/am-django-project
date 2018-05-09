#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
"""
am URL Configuration.
"""

from django.conf.urls import url, include
from django.contrib import admin
from general.views import HomePageView, PersonVotesListView, PersonDetailView, PeopleHomeView
from legislative.views import BillDetailView, VoteDetailView, BillVotesListView, BillTextDetailView, BillsHomeView, BillsTaggedView #noqa
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.conf import settings

from graphene_django.views import GraphQLView

from search.views import BillSearchListView, PersonSearchListView

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', HomePageView.as_view()),
                  url(r'^graphql', GraphQLView.as_view(graphiql=True)),
                  url(r'^bills/$', BillsHomeView.as_view()),
                  url(r'^people/$', PeopleHomeView.as_view()),
                  url(r'^bills/(?P<id>[\w-]+)/$', BillDetailView.as_view(), name='bill'),
                  url(r'^bills/(?P<id>[\w-]+)/votes/$', BillVotesListView.as_view(), name='billvotes'),
                  url(r'^bills/(?P<bill_id>[\w-]+)/votes/(?P<id>[\w-]+)/$', VoteDetailView.as_view(), name='vote'),
                  url(r'^bills/(?P<bill_id>[\w-]+)/text/(?P<id>[\w-]+)/$', BillTextDetailView.as_view(), name='billtext'),
                  url(r'^bills/tagged/(?P<slug>[\w-]+)/$', BillsTaggedView.as_view(), name='billstagged'),
                  url(r'^people/(?P<id>[\w-]+)/$', PersonDetailView.as_view(), name='person'),
                  url(r'^people/(?P<id>[\w-]+)/votes/$', PersonVotesListView.as_view(), name='personvotes'),
                  url(r'^search/bills/', BillSearchListView.as_view(), name='bill-search'),
                  url(r'^search/people/', PersonSearchListView.as_view(), name='person-search'),
                  url(r'^api/', include('api.urls', namespace='api')),
                  url(r'^legislative/', include('legislative.urls', namespace='legislative')),
                  url(r'^finance/', include('finance.urls', namespace='finance')),
                  url(r'^geo/', include('geo.urls', namespace='geo')),
                  url(r'^tags/', include('tags.urls', namespace='tags')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'general.views.handler404'
handler500 = 'general.views.handler500'
