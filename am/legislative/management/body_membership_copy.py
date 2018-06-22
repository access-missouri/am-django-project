#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utility functions for copying BodyMembership rows.
"""

from legislative.models import BodyMembership

def get_or_copy_body_membership_to_session(membership, session):
    """
    Like ModelManager.get_or_create() only for copying BodyMembership.

    :param membership: The BodyMembership to copy.
    :param session: The session to copy into.
    :return: A tuple of the copied(or not) membership and whether it was created.
    """
    membership_copy, created = BodyMembership.objects.get_or_create(
        person=membership.person,
        body=membership.body,
        session=session,
        district=membership.district
    )

    return (membership_copy, created)

def replicate_all_body_memberships_into_session(source, destination):
    """
    Take all the memberships from a given session and make sure they're in the new session.


    :param source: Session to copy BodyMemberships from.
    :param destination: Session to copy BodyMemberships to.
    :return: The number of fresh BodyMemberships created.
    """
    memberships_created = 0

    for membership_old in source.body_memberships:
        membership_new, created = get_or_copy_body_membership_to_session(membership_old,
                                                                         destination)
        if created:
            memberships_created += 1

    return memberships_created
