from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user

class TestLoginEndpoints (TestCase) : 

    def setUp(self):
        self.login_url = reverse('login')
    

    def test_EMPTY_BODY(self) : 
        res = self.client.post(self.login_url)
        self.assertNotEqual(res.status_code, 200)

    def test_INVALID_METHOD(self) : 
        res = self.client.get(self.login_url)
        self.assertNotEqual(res.status_code, 200)
    
    def test_INVALID_DATA(self) : 
        data = {
            'email_or_phonenumber' : 'test@gmail.com',
            'password' : 'test',
        }
        res = self.client.post(self.login_url, data=data)
        self.assertNotEqual(res.status_code, 200)

    def test_INVALID__EMAIL_OR_PHONENUMBER(self) : 
        data = {
            'email_or_phonenumber' : '+201009675001test@gmail.com',
            'password' : 'test',
        }
        res = self.client.post(self.login_url, data=data)
        self.assertNotEqual(res.status_code, 200)

    def test_SUCCESS_LOGIN(self) : 
        email = 'test@gmail.com'
        password = 'test'
        user = create_user(
            username = 'test',
            email = email,
            password = password
        )
        data = {
            'email_or_phonenumber' : user.email,
            'password' : password,
        }
        res = self.client.post(self.login_url, data=data)
        self.assertEqual(res.status_code, 201)
