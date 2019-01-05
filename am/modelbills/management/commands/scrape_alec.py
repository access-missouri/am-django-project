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

        # Loop through all the ALEC model bills index pages, scraping down the urls to further bills.
        alec_page_first = AlecListInterpreter(url="https://www.alec.org/model-policy/")
        model_bill_urls = alec_page_first.bill_urls
        list_page = 2
        while True:
            alec_list_page = AlecListInterpreter(url="https://www.alec.org/model-policy/page/{}/".format(list_page))
            if alec_list_page.response.status_code != 200:
                break
            for url in alec_list_page.bill_urls:
                model_bill_urls.append(url)
            print("Finished index page {}.".format(list_page))
            list_page += 1
        print("Finished pulling bill URLS. {} total.".format(len(model_bill_urls)))
        for url in tqdm(model_bill_urls):
            bill_page = AlecBillInterpreter(url)
            bill, bill_created = ModelBill.objects.get_or_create(
                source_url=url,
                origin=org,
                name=bill_page.name,
                summary=bill_page.summary,
                text=bill_page.text
            )