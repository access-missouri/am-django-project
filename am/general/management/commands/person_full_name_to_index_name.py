#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Concatenates person name fields to the index name field.
"""
from django.core.management.base import BaseCommand
from general.models import Person
from tqdm import tqdm
import requests
import re
from time import sleep


class Command(BaseCommand):
    """
    Concatenates person name fields to the index name field.
    """

    help = 'Concatenates person name fields to the index name field.'

    def handle(self, *args, **options):
        """
        Concatenates person name fields to the index name field.
        """
        qset = Person.objects.filter(index_name=None)

        for person in tqdm(
                iterable=qset,
                total=qset.count()):
            person.index_name = person.get_full_name()
            person.save()

