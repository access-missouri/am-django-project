#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Migrate votes to the membership object link.
"""
from django.core.management.base import BaseCommand
from legislative.models import BodyMembership, PersonVote, LegislativeSession
from django.db import models
from tqdm import tqdm
import django.core.exceptions as ex


class Command(BaseCommand):
    """
    Migrate votes to the membership object link.
    """

    help = 'Migrate votes to the membership object link.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        session_id = input("Choose a session ID: ")
        session = LegislativeSession.objects.get(id=session_id)



        votes = PersonVote.objects.filter(member=None,
                                          bill_vote__bill__legislative_session=session)

        votes_changed = 0

        for vote in tqdm(
                iterable=votes,
                total=votes.count()):
                try:
                    member = BodyMembership.objects.get(
                        person=vote.person,
                        session=session,
                    )
                    vote.member = member
                    vote.save()
                    votes_changed += 1
                except models.ObjectDoesNotExist:
                    pass
                except ex.MultipleObjectsReturned:
                    print("{} has multiple memberships in session.".format(vote.person))
                    pass

        print("{} votes changed.".format(votes_changed))
