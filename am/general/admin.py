#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
General models app admins.
"""
from django.contrib import admin # NOQA

from .models import Organization, Post, Person, Tag

from legislative.models import BodyMembership

admin.site.register(Organization)
admin.site.register(Post)

class BodyMembershipInline(admin.TabularInline):
    model = BodyMembership
    fields = ('body','session','district')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = ((None, {
        'fields': (
            ('first_name','middle_name',),
            'last_name',
            ('nickname','suffix',),
        )
    }),
                 ("Infrequently Used", {
                     'fields': (
                         'extras',
                         'gender',
                         'index_name',
                     ),
                     'classes': ('collapse',)
                 }),
                 )
    inlines = [BodyMembershipInline]
    search_fields = ['index_name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name','slug',)