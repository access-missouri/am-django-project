# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

class SearchBillForm(forms.Form):
    search_name = forms.CharField(required=False)