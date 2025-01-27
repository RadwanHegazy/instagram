from globals.test_objects import create_token_headers, create_user, create_post
from django.test import TestCase
from django.urls import reverse

class TestDeleteEndpoint(TestCase) : 

    def retrive_post_endpoint(self, post_id) : 
        return reverse('delete_post_by_id',args=[post_id])
    
    def setUp(self):
        self.user = create_user(username='test321')

    def test_DELETE_unauthorized (self) : 
        req = self.client.delete(
            self.retrive_post_endpoint(1)
        )
        self.assertEqual(req.status_code, 404)

    def test_DELETE_not_found_post (self) : 
        req = self.client.delete(
            self.retrive_post_endpoint(1),
            headers=create_token_headers(self.user),
        )
        self.assertEqual(req.status_code, 404)

    def test_DELETE_not_owner (self) : 
        user_1 = create_user(username='user011')
        user_2 = create_user(username='user001')
        post = create_post(user_1)

        req = self.client.delete(
            self.retrive_post_endpoint(post.id),
            headers=create_token_headers(user_2),
        )
        self.assertEqual(req.status_code, 403)

    def test_DELETE_is_owner (self) : 
        user_1 = create_user(username='user111')
        # user_2 = create_user(username='user001')
        post = create_post(user_1)

        req = self.client.delete(
            self.retrive_post_endpoint(post.id),
            headers=create_token_headers(user_1),
        )
        self.assertEqual(req.status_code, 204)
