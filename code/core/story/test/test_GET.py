from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_token_headers


class TestGetStoryEndpoint(TestCase) : 

    def get_story_endpint(self, id) : 
        return reverse('get_story', args=[id])

    def setUp(self):
        self.get_stories_endpint = reverse('get_stories')
