#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a folder (~/mec/cd3_c) full of MEC CSV files to the database.
"""
from django.core.management.base import BaseCommand
import os
from tqdm import tqdm

from finance.models import FinanceEntity, FinanceTransaction, MecLink


class Command(BaseCommand):
    """
    Import a folder (~/mec/cd3_c) full of MEC CSV files to the database.
    """

    help = 'Fix hanging MEC entries into one committee body.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        print("This fix hanging MEC entries into one committee body. "
              + "The progress bar may mislead you, but it's still nice to have.")

        for entity_outer in tqdm(
                FinanceEntity.objects.filter(type="comm"),
                total=FinanceEntity.objects.filter(type="comm").count()):
            # Check for duplicates.
            q = FinanceEntity.objects.filter(name__iexact=entity_outer.name)
            if q.count() > 1:
                entity_dupes_array = []

                for entity in q:
                    entity_dupes_array.append(entity)

                entity_canonical = entity_dupes_array.pop()

                for entity in entity_dupes_array:
                    if entity.mec_id:
                        mec_link, link_created = MecLink.objects.get_or_create(
                            mec_id=entity.mec_id,
                            entity=entity
                        )
                    for transaction in entity.income.all():
                        transaction.t_to = entity_canonical
                        transaction.save()
                    for transaction in entity.spending.all():
                        transaction.t_from = entity_canonical
                        transaction.save()
                    entity.delete()