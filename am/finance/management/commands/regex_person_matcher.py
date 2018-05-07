#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manual tagging utility to pair regexes with canonical people on a one-off run.
"""
from django.core.management.base import BaseCommand
from finance.models import FinanceEntity
from general.models import Person
import re
from tqdm import tqdm

class Command(BaseCommand):
    """
    Manual tagging utility to pair regexes with canonical people on a one-off run.
    """

    help = 'Manual tagging utility to pair regexes with canonical people on a one-off run.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        regex_str = raw_input("Enter a Python-style regex to tag with: ")
        id_str = raw_input("Enter a person id: ")
        regex_compiled = re.compile(regex_str)
        person_m = Person.objects.get(id=id_str)

        qset = FinanceEntity.objects.all()

        entities_tagged = 0

        for entity in tqdm(
                iterable=qset,
                total=qset.count()):
            if regex_compiled.search(entity.name):
                # No need to check - doubling up does not duplicate.
                entity.related_people.add(person_m)
                entity.canonical_person = person_m
                entity.save()
                entities_tagged += 1

        print("{} total entities given canonical and related relationships with {} based on r'{}'.".format(
            entities_tagged,
            person_m.get_full_name(),
            regex_str
        ))
