from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_token_headers, create_user, create_post
import os
import json

class TestGetEndpoints(TestCase) : 

    def retrive_post_endpoint(self, post_id) : 
        return reverse('get_post_by_id',args=[post_id])
    
    def retrive_user_post_endpoint(self, username) : 
        return reverse('user_posts', args=[username])
    
    def setUp(self):
        self.get_all_posts_endpoint = reverse('all_posts')

    def test_GET_unauthorized_user(self) : 
        req = self.client.get(
            self.get_all_posts_endpoint
        )
        self.assertEqual(req.status_code, 401)

    def test_GET_authorized_user(self) :
        req = self.client.get(
            self.get_all_posts_endpoint,
            headers=create_token_headers()
        )
        self.assertEqual(req.status_code, 200)

    def test_GET_empty_posts(self) : 
        user = create_user(username='test2')
        user_headers = create_token_headers(user)
        create_post()
        req = self.client.get(
            self.get_all_posts_endpoint,
            headers=user_headers
        )
        self.assertEqual(req.json()['results'], [])

    def test_GET_nonempty_posts(self) : 
        user = create_user(username='test22313')
        user_headers = create_token_headers(user)
        friend = create_user(username='friend')
        for i in range(10) :
            p = create_post(friend)
        user.followings.add(friend)
        user.save()
        req = self.client.get(
            self.get_all_posts_endpoint,
            headers=user_headers
        )
        self.assertNotEqual(req.json(), [])

    def test_GET_retrive_post_unauthorized(self) : 
        req = self.client.get(
            self.retrive_post_endpoint(1),
        )
        self.assertEqual(req.status_code, 401)

    def test_GET_retrive_post_unfounded_post(self) : 
        req = self.client.get(
            self.retrive_post_endpoint(1),
            headers=create_token_headers()
        )
        self.assertEqual(req.status_code, 404)
    
    
    def test_GET_retrive_post_founded_post(self) : 
        user = create_user(username='213')
        post = create_post(user)
        req = self.client.get(
            self.retrive_post_endpoint(post.id),
            headers=create_token_headers(user)
        )
        self.assertEqual(req.status_code, 200)

    def test_GET_retrive_post_check_is_owner(self) : 
        user = create_user(username='test22')
        post = create_post(user)
        req = self.client.get(
            self.retrive_post_endpoint(post.id),
            headers=create_token_headers(user)
        )
        self.assertEqual(req.json()['owner']['id'], user.id)


    def test_GET_retrive_post_unfounded_user(self) : 
        user = create_user(username='213d')
        post = create_post(user)
        req = self.client.get(
            self.retrive_user_post_endpoint('91919')
        )
        self.assertEqual(req.status_code, 404)


    def test_GET_retrive_post_founded_user(self) : 
        user = create_user(username='213d')
        post = create_post(user)
        req = self.client.get(
            self.retrive_user_post_endpoint(user.username)
        )
        self.assertEqual(req.status_code, 200)

