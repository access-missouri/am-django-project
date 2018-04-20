#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manual utility to create a tag from the command line.
"""
from django.core.management.base import BaseCommand
from general.models import Tag
import re
from tqdm import tqdm

class Command(BaseCommand):
    """
    Manual utility to create a tag from the command line.
    """

    help = 'Manual utility to create a tag from the command line.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        tag_name = raw_input("Name the tag: ")
        tag_slug = raw_input("Enter a tag slug: ")

        tag, created = Tag.objects.get_or_create(
            slug=tag_slug,
            defaults={
                'name': tag_name,
            }
        )

        if created:
            print("Tag '{}' created with slug {} and ID {}.".format(
                tag.name,
                tag.slug,
                tag.id
            ))
        else:
            print("It looks like the tag '{}' already exists with that slug.".format(
                tag.name
            ))