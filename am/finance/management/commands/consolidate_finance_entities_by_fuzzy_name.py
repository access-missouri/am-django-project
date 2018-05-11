#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Use fuzzy string matching to consolidate similar MEC entities.
"""
from django.core.management.base import BaseCommand
import os
from tqdm import tqdm
from fuzzywuzzy import fuzz
from search.utils import phrase_to_q_series
from django.db.models import Q, ObjectDoesNotExist

from finance.models import FinanceEntity

# This chunky logic transfers all the data from one finance entity into the new one.
def merge_entity(entity_from, entity_into):
    for person in entity_from.related_people.all():
        entity_into.related_people.add(person)
        entity_from.related_people.remove(person)

    for transaction in entity_from.income.all():
        tqdm.write("Moving income transaction {}.".format(transaction.id))
        transaction.t_to = entity_into
        transaction.save()
    for transaction in entity_from.spending.all():
        tqdm.write("Moving spending transaction {}.".format(transaction.id))
        transaction.t_from = entity_into
        transaction.save()

    for mec_link in entity_from.mec_links.all():
        mec_link.entity = entity_into
        mec_link.save()

    extras = {}
    if any(entity_into.extras):
        extras = entity_into.extras

    priors = []
    if 'priors' in extras:
        priors = extras['priors']
    priors.append({
        "name": entity_from.name,
        "id": entity_from.id,
        "mec_id": entity_from.mec_id,
        "e_type": entity_from.e_type,
        "first_name": entity_from.first_name,
        "last_name": entity_from.last_name,
        "address_first": entity_from.address_first,
        "address_second": entity_from.address_second,
        "address_city": entity_from.address_city,
        "address_state": entity_from.address_state,
        "address_zip": entity_from.address_zip,
        "employer": entity_from.employer,
        "occupation": entity_from.occupation
    })
    extras['priors'] = priors
    entity_into.extras = extras
    entity_into.save()
    entity_from.delete()



class Command(BaseCommand):
    """
    Use fuzzy string matching to consolidate similar MEC entities.
    """

    help = 'Use fuzzy string matching to consolidate similar MEC entities.'


    def handle(self, *args, **options):
        """
        Make it happen.
        """

        entities_merged = 0

        for entity_outer in tqdm(
                FinanceEntity.objects.all()[8000:11000],
                total=FinanceEntity.objects.all()[8000:11000].count()):

            # First, we have to make sure we haven't already removed this entity
            # in one of our previous iterations.
            try:
                FinanceEntity.objects.get(id=entity_outer.id)
            except ObjectDoesNotExist:
                continue


            # Now, we're actually free to check for duplicates
            entity_name_query = phrase_to_q_series(phrase=entity_outer.name,
                                                   column_name='name')
            entity_type_query = Q(e_type=entity_outer.e_type)
            # To match this entity, we know the name and type should be similar.
            match_query = entity_name_query & entity_type_query
            entity_match_list = FinanceEntity.objects.filter(match_query)

            for entity_matched in entity_match_list:
                if entity_matched == entity_outer:
                    continue
                if fuzz.ratio(entity_outer.name, entity_matched.name) >= 97:
                    tqdm.write("Matched {} to {}. This is merge {}.".format(entity_outer,
                                                                            entity_matched,
                                                                            entities_merged))
                    merge_entity(entity_from=entity_matched, entity_into=entity_outer)
                    entities_merged += 1

        print("{} total entities merged.".format(entities_merged))
