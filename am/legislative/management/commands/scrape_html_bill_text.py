#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrapes bill text available in html.
"""
from django.core.management.base import BaseCommand
from legislative.models import BillText
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
from time import sleep

class Command(BaseCommand):
    """
    Scrapes bill text available in html.
    """

    help = 'Scrapes bill text available in html.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        def ingest_bill_text(bill_text):
            result = requests.get(bill_text.state_url)
            c = result.content
            soup = BeautifulSoup(c)

            [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]

            bill_text.text = soup.getText()

            bill_text.save()

        qset = BillText.objects.filter(type='text/html',
                                       text=None)

        for b_text in tqdm(
                iterable=qset,
                total=qset.count()):
            ingest_bill_text(b_text)
            sleep(1)