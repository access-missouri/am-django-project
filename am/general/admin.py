#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
General models app admins.
"""
from django.contrib import admin # NOQA

from .models import Organization, Post, Membership, Person, Tag

admin.site.register(Organization)
admin.site.register(Post)
admin.site.register(Membership)

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

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name','slug',)