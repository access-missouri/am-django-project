# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from general.models import AMBaseModel, Organization

# Create your models here.
class ModelBill(AMBaseModel):
    name = models.CharField(max_length=512,
                            blank=False,
                            null=False)
    origin = models.ForeignKey(Organization,
                               related_name="model_bills")
    summary = models.TextField(blank=True,
                               null=True)
    text = models.TextField()
    source_url = models.URLField(max_length=512,
                                 blank=True,
                                 null=True)

    def get_absolute_url(self):
        return '/modelbills/m/{}'.format(
            self.id,
        )
