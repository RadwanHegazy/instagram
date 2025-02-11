from django.test import TestCase
from globals.test_objects import create_user, create_token_headers, create_notification
from django.urls import reverse

class TestGetNotificaionEndpoint(TestCase) : 

    def setUp(self):
        self.get_endpoint_url = reverse('get_notifications')
        self.user = create_user()

    def test_unauth_user(self) :
        req = self.client.get(self.get_endpoint_url)
        self.assertEqual(req.status_code, 401)

    def test_auth_user(self) : 
        req = self.client.get(self.get_endpoint_url, headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 200)

    def test_empty_response(self) :

        req = self.client.get(self.get_endpoint_url, headers=create_token_headers(self.user))
        self.assertEqual(req.json()['results'], [])

    def test_nonempty_response(self) :
        create_notification(
            self.user,
            create_user('t2'),
        )
        req = self.client.get(self.get_endpoint_url, headers=create_token_headers(self.user))
        self.assertEqual(req.json()['results'], [])
    
    def test_nonempty_response(self) :
        create_notification(
            create_user('t3'),
            self.user,
        )
        req = self.client.get(self.get_endpoint_url, headers=create_token_headers(self.user))
        self.assertNotEqual(req.json()['results'], [])
    