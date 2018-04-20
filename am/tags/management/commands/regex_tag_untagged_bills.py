#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tags untagged bills according to regex pairings.
"""
from django.core.management.base import BaseCommand
from legislative.models import Bill
from general.models import Tag
import re
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
from time import sleep
from django.db.models import Count

class Command(BaseCommand):
    """
    Tags untagged bills according to regex pairings.
    """

    help = 'Tags untagged bills according to regex pairings.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        # Tagset is stored in pattern of [regex,tag]
        tagset = [
            [re.compile('(?i)health'),
             Tag.objects.get(slug='health')],
        ]


        def match_tag_bill(bill, regex_compiled, tag):
            if regex_compiled.search(bill.title):
                bill.tags.add(tag)

        qset = Bill.objects.annotate(c=Count('tags')).filter(c__lt=1)

        for bill in tqdm(
                iterable=qset,
                total=qset.count()):
            for tagpair in tagset:
                match_tag_bill(bill, tagpair[0], tagpair[1])
