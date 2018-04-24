#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Migrate bill sponsorships to the membership object link.
"""
from django.core.management.base import BaseCommand
from general.models import Person
from legislative.models import BodyMembership, BillSponsorship
from geo.models import District
from search import utils
import csv
import os
from django.db import models
from tqdm import tqdm


class Command(BaseCommand):
    """
    Migrate bill sponsorships to the membership object link.
    """

    help = 'Migrate bill sponsorships to the membership object link.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        sponsorships = BillSponsorship.objects.filter(member=None)

        sponsorships_changed = 0

        for sponsorship in tqdm(
                iterable=sponsorships,
                total=sponsorships.count()):
                try:
                    member = BodyMembership.objects.get(
                        person=sponsorship.person,
                        session=sponsorship.bill.legislative_session,
                    )
                    sponsorship.member = member
                    sponsorship.save()
                    sponsorships_changed += 1
                except models.ObjectDoesNotExist:
                    pass

        print("{} sponsorships changed.".format(sponsorships_changed))
