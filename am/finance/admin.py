# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from finance.models import FinanceEntity, FinanceTransaction

# Register your models here.

@admin.register(FinanceEntity)
class FinanceEntityAdmin(admin.ModelAdmin):
    fieldsets = ((None, {
        'fields': (
            ('name', 'type',),
            'mec_id',
            'linked_person',
        )
    }),
                 ("More Info", {
                     'fields': (
                         'first_name',
                         'last_name',
                         'address_first',
                         'address_second',
                         'address_city',
                         'address_state',
                         'address_zip',
                         'employer',
                         'occupation',
                     ),
                     'classes': ('collapse',)
                 }),
                 ("Infrequently Used", {
                     'fields': (
                         'extras',
                     ),
                     'classes': ('collapse',)
                 }),
                 )
