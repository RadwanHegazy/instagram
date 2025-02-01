from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_token_headers, create_story


class TestCreateStoryEndpoint(TestCase) : 

    def setUp(self):
        self.create_stories_endpint = reverse('create_story')
        self.user = create_user(
            username='t1',
            email='t@test.com',
            password='test'
        )
    
    def test_unauthorized_user(self) :
        req = self.client.post(self.create_stories_endpint)
        self.assertEqual(req.status_code, 401)

    def test_invalid_method(self):        
        req = self.client.get(self.create_stories_endpint, headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 405)

    def test_empty_body(self) :
        req = self.client.post(self.create_stories_endpint, headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 400)

    def test_empty_img(self) :
        text_list = """[{"content" : "content is here","color" : "red","x" : 10,"y" : 30}]""" 
        body = {
            'text_list' :text_list, 
        } 
        req = self.client.post(self.create_stories_endpint, headers=create_token_headers(self.user), data=body)
        self.assertEqual(req.status_code, 400)

    def test_empty_text_list(self) :
        body = {
            'image' : open('media/profile.png','rb'), 
        }
        req = self.client.post(self.create_stories_endpint, headers=create_token_headers(self.user), data=body)
        self.assertEqual(req.status_code, 400)

    def test_POST_sucess(self) :
        text_list = """[{"content" : "content is here","color" : "red","x" : 10,"y" : 30}]""" 
        body = {
            'image' : open('media/profile.png','rb'), 
            'text_list' : text_list
        }
        req = self.client.post(self.create_stories_endpint, headers=create_token_headers(self.user), data=body)
        self.assertEqual(req.status_code, 204)