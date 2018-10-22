#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a folder (~/mec) full of MEC CSV files to the database.
"""
from django.core.management.base import BaseCommand
import os
from tqdm import tqdm
from csv import DictReader
from datetime import datetime

from finance.models import FinanceEntity, FinanceTransaction


class Command(BaseCommand):
    """
    Import a folder (~/mec) full of MEC CSV files to the database.
    """

    help = 'Import a folder full of MEC CSV files to the database.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        def csv_to_db(csv_path):
            csv_data = open(csv_path)
            csv = DictReader(csv_data)

            for row in tqdm(csv, total=len(open(csv_path).readlines())):
                to_mec_id = row[" MECID"]
                to_committee_name = row["Committee Name"]

                fr_comm_name = row["Committee"]
                fr_corp_name = row["Company"]
                fr_first_name = row["First Name"]
                fr_last_name = row["Last Name"]
                fr_addr_one = row["Address 1"]
                fr_addr_two = row["Address 2"]
                fr_city = row["City"]
                fr_state = row["State"]
                fr_zip = row["Zip"]
                fr_employer = row["Employer"]
                fr_occupation = row["Occupation"]

                t_date = (datetime
                            .strptime(row["Date"].split(" ")[0], "%m/%d/%Y")
                            .date())
                t_amount = row["Amount"]
                t_con_type = row["Contribution Type"]

                # Avoid object or transaction duplication
                # by looking for confident matches of the given info.
                to_obj = FinanceEntity.entities.get_closest_confident_match(
                    name=to_committee_name,
                    e_type="comm",
                    mec_id=to_mec_id
                )

                # If there are none,
                # proceed to do things the old way.
                if not to_obj:
                    to_obj, to_created = FinanceEntity.objects.get_or_create(
                        name=to_committee_name,
                        e_type="comm",
                        defaults={
                            "mec_id": to_mec_id,
                        }
                    )

                fr_obj, fr_created = None, None

                fr_defaults={
                            "address_first": fr_addr_one,
                            "address_second": fr_addr_two,
                            "address_city": fr_city,
                            "address_state": fr_state,
                            "address_zip": fr_zip,
                            "employer": fr_employer,
                            "occupation": fr_occupation,
                        }

                # For now, we only do confidence matching
                # on committees in the "from" area.
                if fr_comm_name:
                    fr_obj = FinanceEntity.entities.get_closest_confident_match(
                        name=fr_comm_name,
                        e_type="comm",
                        defaults=fr_defaults
                    )
                    # If there are no smart matches,
                    # proceed to do things the old way.
                    if not fr_obj:
                        fr_obj, fr_created = FinanceEntity.objects.get_or_create(
                            name=fr_comm_name,
                            e_type="comm",
                            defaults=fr_defaults
                        )
                elif fr_corp_name:
                    fr_obj, fr_created = FinanceEntity.objects.get_or_create(
                        name=fr_corp_name,
                        e_type="corp",
                        defaults=fr_defaults
                    )
                elif fr_first_name or fr_last_name:
                    fr_defaults['name'] = "{} {}".format(fr_first_name, fr_last_name)
                    fr_obj, fr_created = FinanceEntity.objects.get_or_create(
                        first_name=fr_first_name,
                        last_name=fr_last_name,
                        address_first=fr_addr_one,
                        e_type="person",
                        defaults=fr_defaults
                    )

                t_str = "{} to {} in amount {}.".format(str(fr_obj), str(to_obj), str(t_amount))

                tqdm.write(t_str)

                t_obj, t_created = FinanceTransaction.objects.get_or_create(
                    t_from=fr_obj,
                    t_to=to_obj,
                    e_type=t_con_type,
                    amount=t_amount,
                    date=t_date
                )

                tqdm.write("Created." if t_created else "Already exists.")



        target_directory = os.path.join(os.path.expanduser("~"), 'mec')
        for file in os.listdir(target_directory):
            if file.endswith(".csv"):
                print("Starting {}.".format(file))
                csv_to_db(os.path.join(target_directory, file))
                print("Finished {}.".format(file))
