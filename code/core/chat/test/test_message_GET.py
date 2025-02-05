from django.test import TestCase
from globals.test_objects import create_user, create_token_headers, create_chat, create_message
from django.urls import reverse
from uuid import uuid4

class TestGetChatMessagesEndpoint(TestCase) : 
    
    def get_chat_msgs_endpoints (self, chatid) : 
        return reverse('get_chat_msgs', args=[str(chatid)])
    
    def setUp(self):
        self.user = create_user()
        self.chat = create_chat(
            self.user,
            create_user(username='t2')
        )
    
    def test_unauthorized_user(self) : 
        req = self.client.get(self.get_chat_msgs_endpoints(self.chat.id))
        self.assertEqual(req.status_code, 401)

    def test_not_found_chat(self) : 
        req = self.client.get(self.get_chat_msgs_endpoints(uuid4()), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 404)

    def test_permission_denied_chat(self) :
        new_user = create_user(username='t3')
        req = self.client.get(self.get_chat_msgs_endpoints(self.chat.id), headers=create_token_headers(new_user))
        self.assertEqual(req.status_code, 403)

    def test_empty_chat_messages(self) : 
        req = self.client.get(self.get_chat_msgs_endpoints(self.chat.id), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['results'], [])
    
    def test_non_empty_chat_messages(self) : 
        create_message(
            self.user,
            'test',
            self.chat
        )
        req = self.client.get(self.get_chat_msgs_endpoints(self.chat.id), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['results'], [])
    