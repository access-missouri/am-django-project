#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Legislative models app admins.
"""
from django.contrib import admin # NOQA
from .models import Bill, LegislativeSession, BillAbstract, BillAction, BillAmendment, BillSponsorship, BillTitle, BillVersion   # NOQA

# Register your models here.

admin.site.register(Bill)
admin.site.register(LegislativeSession)
admin.site.register(BillAbstract)
admin.site.register(BillAction)
admin.site.register(BillAmendment)
admin.site.register(BillSponsorship)
admin.site.register(BillTitle)
admin.site.register(BillVersion)
