#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
General models app admins.
"""
from django.contrib import admin # NOQA

from .models import Organization, Post, Membership, Person

admin.site.register(Organization)
admin.site.register(Post)
admin.site.register(Membership)
admin.site.register(Person)