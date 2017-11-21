# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from legislative.models import LegislativeSession
from select2.widgets import SelectMultiple

class SearchBillForm(forms.Form):
    search_name = forms.CharField(required=False,
                                  label="Keywords")
    search_sessions = forms.ModelMultipleChoiceField(
        label="From Sessions",
        required=False,
        queryset= LegislativeSession.objects.all().order_by('name'),
        widget=SelectMultiple,
        initial=LegislativeSession.objects.all(),
    )