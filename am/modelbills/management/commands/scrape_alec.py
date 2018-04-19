#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrape data from the ALEC site and load into model policy models.
"""
from django.core.management.base import BaseCommand

from modelbills.scrapers.interpreters.alec_list import AlecListScraper

class Command(BaseCommand):
    """
    Scrape data from the ALEC site and load into model policy models.
    """

    help = 'Scrape data from the ALEC site and load into model policy models.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        # Loop through all the ALEC model bills index pages, scraping down the urls to further bills.
        alec_page_first = AlecListScraper(url="https://www.alec.org/model-policy/")
        model_bill_urls = alec_page_first.bill_urls
        list_page = 2
        while True:
            alec_list_page = AlecListScraper(url="https://www.alec.org/model-policy/page/{}/".format(list_page))
            if alec_list_page.response.status_code != 200:
                break
            for url in alec_list_page.bill_urls:
                model_bill_urls.append(url)
            print("Finished index page {}.".format(list_page))
            list_page += 1
        print(model_bill_urls)
