#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://senate.mo.gov/.../Bill.aspx.
"""
from senate_scraper.scrapers import BaseScraper
from datetime import datetime


class BillDetailsScraper(BaseScraper):
    """
    Request, cache and parse http://senate.mo.gov/.../Bill.aspx.
    """

    def __init__(self, params, **kwargs):
        """
        Initialize an object for scraping a bill's details page.

        Args:
            params (dict): Key/values sent in the query string when requesting
                the bill's actions.
            **kwargs: Arbitrary keyword arguments.
        """
        super(BillDetailsScraper, self).__init__(
            url_path="Bill.aspx",
            params=params,
            **kwargs
        )

    @property
    def description(self):
        """
        Return the text of the bill's description.
        """
        return self.soup.find('span', id='lblBriefDesc').text.strip()

    @property
    def number(self):
        """
        Return the text of the bill's "number".
        """
        return self.soup.find('span', id='lblBillNum').text.strip()

    @property
    def number_as_int(self):
        """
        Return the integer representation of the bill's "number".
        """
        return int(self.soup.find('span', id='lblBillNum')
                   .text.strip()
                   .split()  # Split into array of strings by space.
                   [-1])  # Take the last one and turn it into an integer.

    @property
    def lr_number(self):
        """
        Return a string representation of the bill's LR number.
        """
        return self.soup.find('span', id='lblLRNum').text.strip()

    @property
    def committee(self):
        """
        Return a unicode string representation of the bill's committee.
        """
        return self.soup.find('a', id='hlCommittee').text.strip()

    @property
    def committee_url(self):
        """
        Return a unicode string representation of the bill's committee URL link.
        """
        return self.soup.find('a', id='hlCommittee')['href']

    @property
    def amendments_url(self):
        """
        Return a unicode string representation of the bill's amendments URL link.
        """
        return self.soup.find('a', id='hlAmends')['href']

    @property
    def actions_url(self):
        """
        Return a unicode string representation of the bill's actions URL link.
        """
        return self.soup.find('a', id='hlAllActions')['href']

    @property
    def full_text_url(self):
        """
        Return a unicode string representation of the bill's full text URL link.
        """
        return self.soup.find('a', id='hlFullBillText')['href']

    @property
    def sponsors(self):
        """
        Get an array of bill sponsor surnames.
        """
        return [a.text.strip() for a in self.soup.find_all('a', id='hlSponsor')]

    @property
    def summary(self):
        """
        Return a unicode string representation of the bill's summary.
        """
        tee_arrs = self.soup.find('table', id='Table5').find_all('tr')
        # Take all the paragraphs inside the last TR and strip them of garbage,
        # then join them into a single string separated by line breaks.
        return "\n".join([x.text.strip() for x in tee_arrs[-1].find_all('p')])

    @property
    def effective_date(self):
        """
        Return the bill's effective date as a Python DateTime.
        """
        eff_date_text = self.soup.find('span', id='lblEffDate').text.strip()
        try:
            return datetime.strptime(eff_date_text, '%B %, %Y').date()
        except ValueError:
            return None

    @property
    def fiscal_notes_url(self):
        """
        Return string URL for the bill's fiscal notes page, or None if doesn't exist.
        """
        try:
            return self.soup.find('a', id='hlFiscalNote')['href']
        except TypeError:
            return None

    @property
    def summaries_url(self):
        """
        Return string URL for the bill's summaries page, or None if doesn't exist.
        """
        try:
            return self.soup.find('a', id='hlSummaries')['href']
        except TypeError:
            return None
