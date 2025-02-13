from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_token_headers

class TestLoginEndpoints (TestCase) : 

    def setUp(self):
        self.follow_endpoint = reverse('follow_user')
        self.unfollow_endpoint = reverse('unfollow_user')
        self.user = create_user('u1')
        self.friend = create_user('u2')

    def test_unauthorized_action (self) : 
        req = self.client.post(self.follow_endpoint)
        self.assertEqual(req.status_code, 401)

    def test_success_follow (self) : 
        req = self.client.post(
            self.follow_endpoint,
            data={
                'follow_user_id' : self.friend.id
            },
            headers=create_token_headers(self.user)
        )

        self.assertIn(self.user, self.friend.followers.all())
        self.assertIn(self.friend, self.user.followings.all())

    def test_success_unfollow (self) : 
        self.user.followings.add(self.friend)
        self.friend.followers.add(self.user)

        self.user.save()
        self.friend.save()

        req = self.client.post(
            self.unfollow_endpoint,
            data={
                'follow_user_id' : self.friend.id
            },
            headers=create_token_headers(self.user)
        )

        self.assertNotIn(self.user, self.friend.followers.all())
        self.assertNotIn(self.friend, self.user.followings.all())

