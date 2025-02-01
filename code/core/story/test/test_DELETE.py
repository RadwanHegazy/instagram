from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_token_headers, create_story


class TestDeleteStoryEndpoint(TestCase) : 

    def delete_story_endpint(self, id) : 
        return reverse('delete_story', args=[id])

    def setUp(self):
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

    def test_delete_unauthrized_user(self) : 
        story = create_story(self.user)
        req = self.client.delete(self.delete_story_endpint(story.id))
        self.assertEqual(req.status_code, 401)
    
    def test_delete_authorized_user_story_not_found(self) : 
        req = self.client.delete(self.delete_story_endpint(999), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 404)
    
    def test_delete_authorized_user_not_owner(self) : 
        story = create_story(self.user)
        req = self.client.delete(self.delete_story_endpint(story.id), headers=create_token_headers(self.friend))
        self.assertEqual(req.status_code, 403)
    
    def test_delete_authorized_user_is_owner(self) : 
        story = create_story(self.user)
        req = self.client.delete(self.delete_story_endpint(story.id), headers=create_token_headers(self.user))
        self.assertEqual(req.status_code, 204)
    