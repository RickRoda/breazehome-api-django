from county_records.models import LienRecord
from county_records.views import LienRecordViewSet
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
# Create your tests here.

class LienRecordTest(APITestCase):

    def test_post_lien(self):
        url = 'http://0.0.0.0:8000/liens/'
        data = {
            'cfn_number': '123',
            'cfn_sequence': '12345',
            'group_id': '12345',
            'recording_date': '03282018',
            'recording_time' : '123001',
            'recording_book' : '001',
            'recording_page' : '001',
            'book_type': 'test',
            'document_pages': '10',
            'append_pages': '1',
            'document_date': '03282018',
            'first_party': 'testfirstparty',
            'first_party_code': '1',
            'cross_party_name': 'testcrossparty',
            'folio_number' : '123456789',
            'modified_date': '03282018'
        }    
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LienRecord.objects.count(),1)

    
    def test_get_lien(self):
        # Ensure we can get a Lien Record through the API #
        url = 'http://0.0.0.0:8000/liens/'
        data = {
            'cfn_number' : '123',
            'cfn_sequence' : '1234567',
            'recording_date' : '03282018',
            'folio_number' : '123456789'
        }    
        response = self.client.post(url, data)
        response = self.client.get (url + '?folio_number__icontains=123456789')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content.decode('utf-8')).cfn_Number, '123')
        self.assertEqual(json.loads(response.content.decode('utf-8')).cfn_sequence, '1234567')
        self.assertEqual(json.loads(response.content.decode('utf-8')).recording_date, '03282018')
        self.assertEqual(json.loads(response.content.decode('utf-8')).folio_number, '123456789')

