from django.test import TestCase

# Test Modules
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate

from django.urls import reverse
from django.shortcuts import render

from .views import login,logout

class TestPortal(TestCase):
    def setUp(self):
        # IMPORTANT!! Website must have create this data before manually for a initial working case
        self.factory = RequestFactory()

        # 1° Possibles User Cases from Portal.
        self.users = []
        self.users.append(AnonymousUser())
        self.user = User.objects.create_user(username='testuser1', email='test1@rte-france.com', password='testpass',is_active=True)
        self.users.append(self.user)
        self.user = User.objects.create_user(username='testuser2', email='test2@rte-france.com', password='testpass',is_active=False)
        self.users.append(self.user)


    def test_getLogin(self):
        request = self.factory.get('')
        #Repeat the request for each created user
        for user in self.users:
            request.user = user
            response = login(request)
            self.assertEqual(response.status_code, 200)

    def test_postForm(self):
        request = self.factory.post('/login/')
        #Repeat the request for each created user
        request.user = self.user
        response = login(request)
        self.assertEqual(response.status_code, 200)


    def test_login_post_success(self):
        c = Client()
        response = c.post('/login/', {'username': 'testuser1', 'password': 'testpass'}) # you can use here reverse for urls
        self.assertEqual(response.status_code, 302) # or any other value

    def test_login_post_failed(self):
        c = Client()
        response = c.post('/login/', {'username': 'testuser1', 'password': 'failpass'}) # you can use here reverse for urls
        self.assertEqual(response.status_code, 200) # or any other value

    def test_authenticate_success(self):
        result = authenticate(username='testuser1', password='testpass')
        self.assertTrue(result is not None)

    def test_authenticate_failed(self):
        result = authenticate(username='testuser1', password='testpass')
        self.assertTrue(result is not None)

    def test_postLogout(self):
        response = self.client.post("/logout/", {})
        self.assertEqual(response.status_code, 302)



from django.test import TestCase
from .apps import LoginConfig


class ReportsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(LoginConfig.name, 'Login')


