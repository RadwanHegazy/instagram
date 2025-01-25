from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_token_headers

class TestProfileEndpoints (TestCase) : 

    def setUp(self):
        self.profile_url = reverse('profile')

    def test_UNAUTHORIZED(self) : 
        res = self.client.get(self.profile_url)
        self.assertEqual(res.status_code, 401)
    
    
    def test_SUCCESS_TOKENS(self) : 
        headers = create_token_headers()
        res = self.client.get(self.profile_url, headers=headers)
        self.assertEqual(res.status_code, 200)
