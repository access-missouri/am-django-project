#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Finance Entity and related models.
"""
from __future__ import unicode_literals
from datetime import datetime
from general.models import AMBaseModel
from django.db import models
from general.models import Person

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class FinanceEntity(AMBaseModel):
    """
    A person or thing spending or taking money in Missouri politics.
    """

    mec_id = models.CharField(
        max_length=128,
        help_text='Missouri Ethics Commission ID number.',
        blank=True,
    )
    name = models.CharField(
        max_length=300,
        help_text='Readable name if Company or Committee.'
    )
    ENTITY_TYPE_CHOICES = (
        ('corp', 'Company'),
        ('comm', 'Committee'),
        ('person', 'Person'),
    )
    type = models.CharField(
        max_length=8,
        choices=ENTITY_TYPE_CHOICES,
        null=False,
        blank=False,
        help_text="Company, Committee, or Person?"
    )
    first_name = models.CharField(
        max_length = 75,
        null=True,
        blank=True,
        help_text="First name, if person."
    )
    last_name = models.CharField(
        max_length = 75,
        null=True,
        blank=True,
        help_text="First name, if person."
    )
    address_first = models.CharField(
        max_length = 150,
        null=True,
        blank=True,
    )
    address_second = models.CharField(
        max_length = 150,
        null=True,
        blank=True,
    )
    address_city = models.CharField(
        max_length = 150,
        null=True,
        blank=True,
    )
    address_state = models.CharField(
        max_length = 3,
        null=True,
        blank=True,
    )
    address_zip = models.CharField(
        max_length = 10,
        null=True,
        blank=True,
    )
    employer = models.CharField(
        max_length = 150,
        null=True,
        blank=True,
        help_text="Employer, if person."
    )
    occupation = models.CharField(
        max_length = 150,
        null=True,
        blank=True,
        help_text="Occupation, if person."
    )
    linked_person = models.ForeignKey(Person,
                                      related_name="finance_entities",
                                      null=True,
                                      blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def get_total_income_from_type(self, type):
        sum = self.income.filter(
            t_from__type=type
        ).aggregate(models.Sum('amount'))['amount__sum']
        return sum if sum else 0

    def get_total_income_from_comm(self):
        return self.get_total_income_from_type('comm')

    def get_total_income_from_corp(self):
        return self.get_total_income_from_type('corp')

    def get_total_income_from_people(self):
        return self.get_total_income_from_type('person')

    def get_total_spending_to_type(self, type):
        sum = self.spending.filter(
            t_to__type=type
        ).aggregate(models.Sum('amount'))['amount__sum']
        return sum if sum else 0

    def get_total_spending_to_comm(self):
        return self.get_total_spending_to_type('comm')

    def get_total_spending_to_corp(self):
        return self.get_total_spending_to_type('corp')

    def get_total_spending_to_people(self):
        return self.get_total_spending_to_type('person')

    def get_admin_url(self):
        return "/admin/finance/financeentity/{}/".format(self.id)

    def get_absolute_url(self):
        pl_type = "committees"
        if self.type == "corp":
            pl_type = "companies"
        elif self.type == "person":
            pl_type = "people"
        return "/finance/{}/{}".format(pl_type, self.id)


@python_2_unicode_compatible
class MecLink(AMBaseModel):
    """
    Link multiple MEC ids to one entity.
    """

    mec_id = models.CharField(
        max_length=128,
        help_text='Missouri Ethics Commission ID number.',
        unique=True
    )
    entity = models.ForeignKey(
        FinanceEntity
    )

    def __str__(self):
        return "{}  - {}".format(self.mec_id,self.entity)
