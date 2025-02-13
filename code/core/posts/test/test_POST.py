from globals.test_objects import create_token_headers, create_user, create_post


from django.test import TestCase
from django.urls import reverse

class TestPostEndpoint(TestCase) : 

    def setUp(self):
        self.create_post_endpoint = reverse('create_post')
        self.user = create_user(username='test321')
        self.love_post_endpoint = reverse('add_love')
        self.unlove_post_endpoint = reverse('remove_love')


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
    
    def test_unauthorized_user (self) : 
        req = self.client.post(self.love_post_endpoint)
        self.assertEqual(req.status_code, 401)

    
    def test_sucess_love_post (self) : 
        post = create_post(self.user)
        friend = create_user('friend2')
        before_like = post.likes_by_counter

        req = self.client.post(
            self.love_post_endpoint,
            data={
                'post_id' : post.id
            },
            headers=create_token_headers(friend)
        )

        self.assertIn(friend, post.likes_by.all())
        
    def test_sucess_love_post (self) : 
        post = create_post(self.user)
        friend = create_user('friend2')

        req = self.client.post(
            self.love_post_endpoint,
            data={
                'post_id' : post.id
            },
            headers=create_token_headers(friend)
        )

        self.assertIn(friend, post.likes_by.all())
    
    def test_sucess_unlove_post (self) : 
        post = create_post(self.user)
        friend = create_user('friend2')

        post.likes_by.add(friend)
        post.likes_by_counter += 1
        post.save()
        
        req = self.client.post(
            self.unlove_post_endpoint,
            data={
                'post_id' : post.id
            },
            headers=create_token_headers(friend)
        )

        self.assertNotIn(friend, post.likes_by.all())
        

