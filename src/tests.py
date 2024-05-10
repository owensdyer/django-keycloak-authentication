from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from allauth.socialaccount.models import SocialApp, SocialAccount
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class KeycloakLoginTestCase(TestCase):
    def setUp(self):
        site = Site.objects.get_current()
        self.social_app = SocialApp.objects.create(
            provider='openid', name='University', client_id='napier',
            secret='CzGQFyHxIIGEUeBHwQpxvzn8J92GYAmJ', key='g$cvv$*$zjm$y03a6h(%giwip6+^sh#@jjn5!zym5j*!-^b^%m'
        )

        self.user = User.objects.create_user(username='TestUser', email='Test@pancakes.com', password='PancakesTesting')
        self.social_account = SocialAccount.objects.create(
            user=self.user, provider='openid'
        )

    @patch('requests.post')
    def testSucessfulLogin(self, mockPost):
        mockPost.return_value.json.return_value = {
            'access_token': 'mocked_access_token',
            'refresh_token': 'mocked_refresh_token',
            'token_type': 'Bearer',
            'expires_in': 3600
        }
        mockPost.return_value.status_code = 200

       
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.user.is_authenticated)
        
    @patch('requests.post')
    def testSucessfulLogout(self, mockPost):
        mockPost.return_value.json.return_value = {
            'access_token': 'mocked_access_token',
            'refresh_token': 'mocked_refresh_token',
            'token_type': 'Bearer',
            'expires_in': 3600
        }
        mockPost.return_value.status_code = 302

       
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user.is_authenticated)
        
        
    @patch('requests.post')
    def testClientID(self, mockPost):
        mockPost.return_value.json.return_value = {
            'access_token': 'mocked_access_token',
            'refresh_token': 'mocked_refresh_token',
            'token_type': 'Bearer',
            'expires_in': 3600
            }
            
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
        mockPost.return_value.status_code = 200
        self.assertTrue(SocialApp.secret, 'CzGQFyHxIIGEUeBHwQpxvzn8J92GYAmJ')
            
        

       
        
        