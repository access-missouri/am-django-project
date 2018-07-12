#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Merge MEC Entities.
"""
from tqdm import tqdm

# This chunky logic transfers all the data from one finance entity into the new one.
def merge_entity(entity_from, entity_into):
    """
    Merge two MEC entities.
    :param entity_from:
    :param entity_into:
    :return:
    """
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
