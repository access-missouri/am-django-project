#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrape data from the ALEC site and load into model policy models.
"""
from django.core.management.base import BaseCommand

from tqdm import tqdm

from modelbills.scrapers.interpreters.alec_list import AlecListInterpreter
from modelbills.scrapers.interpreters.alec_bill import AlecBillInterpreter
from general.models import Organization
from modelbills.models import  ModelBill

class Command(BaseCommand):
    """
    Scrape data from the ALEC site and load into model policy models.
    """

    help = 'Scrape data from the ALEC site and load into model policy models.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        org, org_created = Organization.objects.get_or_create(name="American Legislative Exchange Council")

        query = ModelBill.objects.filter(origin=org,
                                         text="")
        for bill in tqdm(iterable=query,
                        total=query.count()):
            bill_page = AlecBillInterpreter(bill.source_url)
            bill.text = bill_page.text
            bill.save()