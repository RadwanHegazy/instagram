from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user

class TestRegisterEndpoints (TestCase) : 

    def setUp(self):
        self.register_url = reverse('register')
    

    def test_EMPTY_BODY(self) : 
        res = self.client.post(self.register_url)
        self.assertNotEqual(res.status_code, 200)

    def test_INVALID_METHOD(self) : 
        res = self.client.get(self.register_url)
        self.assertNotEqual(res.status_code, 200)
    
    def test_ALREADY_USERNAME_DATA(self) : 
        user = create_user()
        data = {
            "username": user.username,
            "phonenumber": "+201009675000",
            "full_name": "Test",
            "password": "test"
        }
        res = self.client.post(self.register_url, data=data)
        self.assertNotEqual(res.status_code, 200)

    def test_SUCCESS_LOGIN(self) : 
        data = {
            "username": "test2",
            "phonenumber": "+201009675000",
            "full_name": "Test",
            "password": "test"
        }
        res = self.client.post(self.register_url, data=data)
        self.assertEqual(res.status_code, 201)
