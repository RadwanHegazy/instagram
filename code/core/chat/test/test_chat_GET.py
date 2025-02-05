from django.test import TestCase
from globals.test_objects import create_user, create_token_headers, create_chat
from django.urls import reverse

class TestGetChatEndpoint(TestCase) : 
    
    def setUp(self):
        self.user = create_user()
        self.get_user_chats_endpoints = reverse('user_chats')

    def test_unauthorized_user(self) : 
        req = self.client.get(self.get_user_chats_endpoints)
        self.assertEqual(req.status_code, 401)


    def test_authorized_user_empty_response (self) : 
        req = self.client.get(self.get_user_chats_endpoints, headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['results'], [])

    
    def test_authorized_user_not_empty_response (self) :
        create_chat(
            self.user,
            create_user(username='t-1')
        )
        req = self.client.get(self.get_user_chats_endpoints, headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['results'], [])


    def test_authorized_user_empty_response_after_creating_chat (self) : 
        create_chat(
            create_user(username='t-0'),
            create_user(username='t-1')
        )
        req = self.client.get(self.get_user_chats_endpoints, headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['results'], [])
