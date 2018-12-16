import os
import sys
import django
import csv
from django.conf import settings

sys.path.append("/home/breazer/breaze/breaze-api-django")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'breaze.settings')
django.setup()
# Miami Dade Records CSV Parser/Importer Version 1.0
# Author - Richard Roda
# Description - This script will parse CSV data given from the Miami-Dade Records
# FTP-API, create the Django Model for each County Record, and insert that County Record into 
# the BreazeHome CountyRecords database.It will also place Lien Records into a seperate
# Lien Model, and insert that Lien Record into the BreazeHome Liens database

def parseRecords(filename):
    # counter for the total number of records in the CSV file
    totalRecords=0
    # counter for the total number of new records added to the database
    newRecord = 0
    # counter for the total number of updated records added to the database
    updatedRecord = 0
    # import the CountyRecord model
    from county_records.models import CountyRecord, LienRecord
    # open the file passed as the parameter in the method call #
    with open(filename) as csvfile:
    # open csv reader and set carat (^) delimiter
        records = csv.reader(csvfile, delimiter='^')
    # skip header #
        next(records,None)
    # for each line in records #
        for line in records:
        #create a new CountyRecord and parse its data
        #the strip() command on some fields is to remove excessive whitespace, if any
            record, created = CountyRecord.objects.get_or_create(
                cfn_number=line[0], 
                cfn_sequence=line[1], 
                group_id=line[2], 
                recording_date=line[3], 
                recording_time=line[4],
                recording_book=line[5],
                recording_page=line[6], 
                book_type=line[7].strip(), 
                document_pages=line[8], 
                append_pages=line[9], 
                document_type=line[10].strip(),
                document_type_description=line[11].strip(),
                document_date=line[12],
                first_party=line[13].strip(),
                first_party_code=line[14],
                cross_party_name=line[15].strip(),
                original_cfn_year=line[16],
                original_cfn_sequence=line[17],
                original_recording_book=line[18],
                original_recording_page=line[19],
                original_misc_reference=line[20].strip(),
                subdivision_name=line[21].strip(),
                folio_number=line[22],
                legal_description=line[23].strip(),
                section=line[24].strip(),
                township=line[25].strip(),
                range=line[26].strip(),
                plat_book=line[27],
                plat_page=line[28],
                block=line[29].strip(),
                case_number=line[30].strip(),
                consideration_one=line[31],
                consideration_two=line[32],
                deed_doc_tax=line[33],
                single_family=line[34],
                surtax=line[35],
                intangible=line[36],
                doc_stamps=line[37],
                key=line[38],
                transaction_type=line[39],
                party_sequence=line[40],
                modified_date=line[41])

            #if the current record is a Lien,create a Lien Record #
            if line[10].strip() == 'LIE':
                lienrecord, liencreated = LienRecord.objects.get_or_create(
                cfn_number=line[0], 
                cfn_sequence=line[1], 
                group_id=line[2], 
                recording_date=line[3], 
                recording_time=line[4],
                recording_book=line[5],
                recording_page=line[6], 
                book_type=line[7].strip(), 
                document_pages=line[8], 
                append_pages=line[9], 
                document_type_description=line[11].strip(),
                document_date=line[12],
                first_party=line[13].strip(),
                first_party_code=line[14],
                cross_party_name=line[15].strip(),
                folio_number=line[22],
                modified_date=line[41])
                
                #save lien Record to Lien Table #
                lienrecord.save()

        #save County Record into County Record Table #
            record.save()
        # increment Record counters #
            if (created):
                totalRecords +=1
                newRecord += 1
            else:
                totalRecords +=1
                updatedRecord+=1
    # parsing complete, close the file #
    csvfile.close()
    return totalRecords, newRecord, updatedRecord
