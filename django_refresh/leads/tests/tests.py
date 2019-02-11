from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from leads.models import Lead

# Create your tests here.

class ApiTestSuite(APITestCase):

    def test_get_method(self):

        response = self.client.get('/api/leads/', format='json')
        print('TEST1: Testing GET method')
        print("Actual response: ", response.status_code)
        print("Expected response: ", status.HTTP_200_OK)

        self.assertEqual(response.status_code, status.HTTP_200_OK)      

        
    def test_post_method(self):
        
        data = {
            "name": "John Doe",
            "email": "jdoe@gmail.com",
            "message": "what's up"
        }

        response = self.client.post('/api/leads/', data, format='json')

        print('\nTEST2: Testing POST method')
        print("Actual response: ", response.status_code)
        print("Expected response: ", status.HTTP_201_CREATED)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
