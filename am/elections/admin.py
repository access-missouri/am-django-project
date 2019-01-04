# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(RaceCandidate)
class RaceCandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(RaceResultHistory)
class RaceResultHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BallotMeasure)
class BallotMeasureAdmin(admin.ModelAdmin):
    pass


@admin.register(ElectionDataSource)
class ElectionDataSourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    pass
