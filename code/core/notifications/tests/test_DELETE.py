from django.test import TestCase
from globals.test_objects import create_user, create_token_headers, create_notification
from django.urls import reverse

class TestDeleteNotificaionEndpoint(TestCase) : 

    def delete_endpoint_url (self, id) : 
        return reverse('delete_notification', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.friend = create_user('t2')

        self.is_reciver_notificaion = create_notification(
            self.friend,
            self.user
        )

        self.is_sender_notification = create_notification(
            self.user,
            self.friend
        )

    def test_unauth_user(self) :
        req = self.client.delete(self.delete_endpoint_url(1))
        self.assertEqual(req.status_code, 401)

    def test_unfounded_notificaion (self) : 
        req = self.client.delete(self.delete_endpoint_url(999), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 404)

    def test_auth_user_not_reciver(self) : 
        req = self.client.delete(self.delete_endpoint_url(self.is_sender_notification.id), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 404)

    def test_delete_success (self) : 
        req = self.client.delete(self.delete_endpoint_url(self.is_reciver_notificaion.id), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 204)
        