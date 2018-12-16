from rest_framework import viewsets
import rest_framework_filters as filters
from .models import CountyRecord, LienRecord
# Richard Roda
# The following filters pertain to the Lien Search feature on BreazeHome

class CountyRecordFilter(filters.FilterSet):
    class Meta:
        model = CountyRecord
        fields = {
            'cfn_number': '__all__',
            'cfn_sequence': '__all__',
            'group_id': '__all__',
            'recording_date': '__all__',
            'recording_time' : '__all__',
            'recording_book' : '__all__',
            'recording_page' : '__all__',
            'book_type': '__all__',
            'document_pages': '__all__',
            'append_pages': '__all__',
            'document_type': '__all__',
            'document_type_description': '__all__',
            'document_date': '__all__',
            'first_party': '__all__',
            'first_party_code': '__all__',
            'cross_party_name': '__all__',
            'original_cfn_year': '__all__',
            'original_cfn_sequence': '__all__',
            'original_recording_book': '__all__',
            'original_recording_page': '__all__',
            'original_misc_reference': '__all__',
            'subdivision_name': '__all__',
            'folio_number': '__all__',
            'legal_description': '__all__',
            'section': '__all__',
            'township': '__all__',
            'range': '__all__',
            'plat_book': '__all__',
            'plat_page': '__all__',
            'block': '__all__',
            'case_number': '__all__',
            'consideration_one': '__all__',
            'consideration_two': '__all__',
            'deed_doc_tax': '__all__',
            'single_family': '__all__',
            'surtax': '__all__',
            'doc_stamps': '__all__',
            'key': '__all__',
            'transaction_type': '__all__',
            'party_sequence': '__all__',
            'modified_date': '__all__'          
        }

class LienRecordFilter(filters.FilterSet):
    class Meta:
        model = LienRecord
        fields = {
            'cfn_number': '__all__',
            'cfn_sequence': '__all__',
            'group_id': '__all__',
            'recording_date': '__all__',
            'recording_time' : '__all__',
            'recording_book' : '__all__',
            'recording_page' : '__all__',
            'book_type': '__all__',
            'document_pages': '__all__',
            'append_pages': '__all__',
            'document_date': '__all__',
            'first_party': '__all__',
            'first_party_code': '__all__',
            'cross_party_name': '__all__',
            'folio_number' : '__all__',
            'modified_date': '__all__'

        }