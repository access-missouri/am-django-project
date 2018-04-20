#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Legislative models app admins.
"""
from django.contrib import admin # NOQA
from .models import Bill, LegislativeSession, BillAbstract, BillAction, BillSponsorship, BillVersion   # NOQA


# Register your models here.


class BillActionInline(admin.TabularInline):
    model = BillAction
    fieldsets = ((None, {
        'fields': (
            'order',
            'date',
            'description',
        )
    }),)


    def get_form(self, request, obj=None, **kwargs):
        form = super(BillActionInline, self).get_form(request, obj, **kwargs)
        form.base_fields['description'].widget.attrs['style'] = 'height: 3em;'
        return form

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    inlines = [BillActionInline,]
    list_display = ['identifier','title','legislative_session','last_action_date']
    search_fields = ['identifier','title','description','legislative_session__name']
    list_filter = ['last_action_date','legislative_session','from_organization']
    filter_horizontal = ['tags',]
    fieldsets = (
        (None, {
            'fields': (
                ('identifier', 'legislative_session',),
                'from_organization',
                'title',
                'description',
                'tags',
                ('last_action_date','last_action_description'),
            )
        }),
        ("Infrequently Used", {
            'fields': (
                'extras',
                'lr_number',
                'calendar_position',
                'proposed_effective_date',
            ),
            'classes': ('collapse',)
        })
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(BillAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['title'].widget.attrs['style'] = 'height: 3em;'
        return form


admin.site.register(LegislativeSession)
admin.site.register(BillAbstract)
admin.site.register(BillAction)
admin.site.register(BillSponsorship)
admin.site.register(BillVersion)