from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_token_headers, create_story


class TestGetStoryEndpoint(TestCase) : 

    def get_story_endpint(self, id) : 
        return reverse('get_story', args=[id])

    def setUp(self):
        self.get_stories_endpint = reverse('get_stories')
        self.user = create_user(
            username='t1',
            email='t@test.com',
            password='test'
        )
        self.friend = create_user(
            username='t2',
            email='t2@test.com',
            password='test2'
        )

    def test_GET_all_stories_unauhorized (self) :
        req = self.client.get(self.get_stories_endpint)
        self.assertEqual(req.status_code, 401)

    def test_GET_all_stories_authorized(self) : 
        req = self.client.get(self.get_stories_endpint, headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 200)
    
    def test_GET_empty_stories_list(self) : 
        req = self.client.get(self.get_stories_endpint, headers=create_token_headers(self.user))
        create_story(self.friend)
        self.assertEqual(req.json()['results'], [])

    def test_GET_nonempty_stories_list(self) : 
        self.user.followings.add(self.friend)
        self.user.save()
        create_story(self.friend)
        req = self.client.get(self.get_stories_endpint, headers=create_token_headers(self.user))
        self.assertNotEqual(req.json()['results'], [])
    
    def test_RETRIVE_story_unauthorized(self) : 
        req = self.client.get(self.get_story_endpint(1))
        self.assertEqual(req.status_code, 401)
    
    def test_RETRIVE_story_authorized_not_found(self) : 
        req = self.client.get(self.get_story_endpint(100), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 404)
    

    def test_RETRIVE_story_authorized_found(self) : 
        story = create_story(self.user)
        req = self.client.get(self.get_story_endpint(story.id), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 200)
    
    