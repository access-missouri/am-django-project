#!/usr/bin/env python
# -*- coding: utf-8 -*-

from senate_scraper.scrapers import BillDetailsScraper, parse_query_str

from params_from_bill import params_from_bill

def update_senate_bill(bill=None, bill_url=None, session=None):
    """
    Update a senate bill given either its existing model or a bill URL and session.
    """

    url_params = {}

    if bill:
        url_params = params_from_bill(bill)
        bill_scraper = BillDetailsScraper(url_params)

        bill.title = bill_scraper.description
        bill.identifier = bill_scraper.number
        bill.lr_number = bill_scraper.params['BillID'],
        bill.proposed_effective_date = bill_scraper.effective_date
        bill.save()
        
    elif bill_url:
        url_params = parse_query_str(bill_url)
        bill_scraper = BillDetailsScraper(url_params)

        bill, created = bill.update_or_create(
            lr_number=bill_scraper.params['BillID'],
            session=session,
            defaults={
                'proposed_effective_date': bill_scraper.effective_date,
                'title': bill_scraper.description,
            },
        )

    return
