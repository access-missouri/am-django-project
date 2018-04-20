#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manual tagging utility to pair regexes with tags on a one-off run.
"""
from django.core.management.base import BaseCommand
from legislative.models import Bill
from general.models import Tag
import re
from tqdm import tqdm

class Command(BaseCommand):
    """
    Manual tagging utility to pair regexes with tags on a one-off run.
    """

    help = 'Manual tagging utility to pair regexes with tags on a one-off run.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        regex_str = raw_input("Enter a Python-style regex to tag with: ")
        tag_slug_str = raw_input("Enter a tag slug: ")
        regex_compiled = re.compile(regex_str)
        tag_m = Tag.objects.get(slug=tag_slug_str)

        qset = Bill.objects.all()

        bills_tagged = 0

        for bill in tqdm(
                iterable=qset,
                total=qset.count()):
            if regex_compiled.search(bill.title):
                # No need to check - doubling up does not duplicate.
                bill.tags.add(tag_m)
                bills_tagged += 1

        print("{} total bills tagged {} based on r'{}'.".format(
            bills_tagged,
            tag_m.name,
            regex_str
        ))
