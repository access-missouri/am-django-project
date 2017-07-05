#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get URL params dict from a bill model.
"""


def params_from_bill(bill):
    """
    Get URL params dict from a bill model.
    """
    return {
        'BillID': bill.lr_number,
        'SessionType': bill.legislative_session.web_session_type_code,
    }
