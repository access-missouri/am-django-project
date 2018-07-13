#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Index all current and previous MEC codes into their own model.
"""
from django.core.management.base import BaseCommand
import os
from tqdm import tqdm

from finance.models import FinanceEntity, FinanceTransaction, MecLink
from finance.management import merge_entities


class Command(BaseCommand):
    """
    Index all current and previous MEC codes into their own model.
    """

    help = 'Index all current and previous MEC codes into their own model.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        print("This fix hanging MEC entries into one committee body. "
              + "The progress bar may mislead you, but it's still nice to have.")

        total_links_created = 0

        for entity in tqdm(
                FinanceEntity.objects.filter(e_type="comm"),
                total=FinanceEntity.objects.filter(e_type="comm").count()):
            # Check for duplicates.
            if entity.mec_id:
                link, created = MecLink.objects.get_or_create(
                    mec_id=entity.mec_id,
                    defaults={
                     'entity': entity,
                    }
                )
                if created:
                    total_links_created += 1
                    tqdm.write("Link created.")
                # If the MEC entity is not the same, merge them.
                elif link.entity.id != entity.id:
                    merge_entities.merge_entity(entity_from=entity, entity_into=link.entity)
                    tqdm.write("Merged {} to {}.".format(entity.name, link.entity.name))
                else:
                    tqdm.write("Link already exists.")

            if 'priors' in entity.extras:
                for prior in 'priors':
                    if 'mec_id' in prior:
                        link, created = MecLink.objects.get_or_create(
                            mec_id=prior['mec_id'],
                            entity=entity
                        )
                        if created:
                            total_links_created += 1

        print("Done. Total links created: ${}".format(total_links_created))
