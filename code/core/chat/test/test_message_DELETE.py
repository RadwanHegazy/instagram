from django.test import TestCase
from globals.test_objects import create_user, create_token_headers, create_chat, create_message, Message
from django.urls import reverse
from uuid import uuid4

class TestDeleteChatMessageEndpoint(TestCase) : 
    
    def delete_msg_endpoint (self, chatid) : 
        return reverse('delete_msg', args=[str(chatid)])
    
    def setUp(self):
        self.user = create_user()
        self.chat = create_chat(
            self.user,
            create_user(username='t2')
        )
        self.message = create_message(
            self.user,
            'test',
            self.chat
        )
    
    def test_unauthorized_user(self) : 
        req = self.client.delete(self.delete_msg_endpoint(self.message.id))
        self.assertEqual(req.status_code, 401)

    def test_not_found_message(self) : 
        req = self.client.delete(self.delete_msg_endpoint(999), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 404)

    def test_permission_delete_chat(self) :
        new_user = create_user(username='t3')
        req = self.client.delete(self.delete_msg_endpoint(self.message.id), headers=create_token_headers(new_user))
        self.assertEqual(req.status_code, 404)

    def test_delete_message_successfully(self) :
        req = self.client.delete(self.delete_msg_endpoint(self.message.id), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 204)
