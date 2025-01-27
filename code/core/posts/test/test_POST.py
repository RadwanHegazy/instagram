from globals.test_objects import create_token_headers, create_user, create_post


from django.test import TestCase
from django.urls import reverse

class TestPostEndpoint(TestCase) : 

    def setUp(self):
        self.create_post_endpoint = reverse('create_post')
        self.user = create_user(username='test321')

    def test_POST_unauthorized (self) : 
        req = self.client.post(
            self.create_post_endpoint
        )
        self.assertEqual(req.status_code, 401)

    def test_POST_empty_body (self) : 
        req = self.client.post(
            self.create_post_endpoint,
            headers=create_token_headers(self.user),
            data={}
        )
        self.assertEqual(req.status_code, 400)

    def test_POST_success (self) : 
        img = open('media/profile.png', 'rb')

        req = self.client.post(
            self.create_post_endpoint,
            headers=create_token_headers(self.user),
            data={
                'body' : 'my testing body',
                'images' : [img]
            },
        )
        
        self.assertEqual(req.status_code, 201)
    