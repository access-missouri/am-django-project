# -*- coding: utf-8 -*-
"""
Custom model manager for finance entities.
"""
from django.db import models
from search.utils import phrase_to_q_series

class EntityQuerySet(models.QuerySet):
    """
    A custom finance entity queryset designed to handle common filtering needs.
    """
    def companies(self):
        return self.filter(e_type='corp')

    def committees(self):
        return self.filter(e_type='comm')

    def people(self):
        return self.filter(e_type='person')


class FinanceEntityManager(models.Manager):
    """
    A custom finance entity model manager that's going to live under "entities."
    """
    def get_query_set(self):
        return EntityQuerySet(self.model)

    def companies(self):
        """
        Get company FinanceEntities.
        :return: A custom QuerySet of only FinanceEntity companies.
        """
        return self.get_query_set().companies()

    def committees(self):
        """
        Get committee FinanceEntities.
        :return: A custom QuerySet of only FinanceEntity committees.
        """
        return self.get_query_set().committees()

    def people(self):
        """
        Get person FinanceEntities.
        :return: A custom QuerySet of only FinanceEntity people.
        """
        return self.get_query_set().people()

    def get_closest_confident_match(self, **kwargs):
        """
        Get what Access Missouri's algorithms believe
        to be the closest matching FinanceEntity
        with a reasonable degree of confidence.

        :param \**kwargs: Every piece of info you can provide,
        formatted like you would for exact matches in .filter().
        :return: Returns a single FinanceEntity, or None if there is no confident match.
        :rtype: Individual FinanceEntity model. None if no match.
        """

        query_set = self.get_query_set()

        if 'e_type' in kwargs:
            query_set = query_set.filter(e_type = kwargs['e_type'])

        if 'name' in kwargs:
            name_string = kwargs['name']
            query_set_new = query_set.filter(phrase_to_q_series(name_string, column_name='name'))

            # Test if there are actually any results here.
            qs_new_count = query_set_new.count()
            if qs_new_count == 1:
                # If this is the only result, we can be reasonably confident it's right.
                # In the future, we'll add address filtering for edge cases.
                return query_set_new[0]
            else:
                # If we have no results, we'll filter again, this time on prior names.
                query_set_new = query_set.filter(phrase_to_q_series(name_string, column_name='extras__priors'))
                qs_new_count = query_set_new.count()
                if qs_new_count == 1:
                    return query_set_new[0]
                elif qs_new_count < 1:
                    # Now, at this point, if nothing has worked, but they provided a name,
                    # it's time to assume we can't be confident.
                    return None
            # If we get down this far, that's because there were multiple matches.
            # Time to filter further.
            query_set = query_set_new

        return None
