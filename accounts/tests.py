from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import signup
from .forms import SignUpForm

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,SignUpForm)

    def test_signup_url_resolves_signup_view(self):
        view = resolve ('/signup/')
        self.assertEquals(view.func,signup)

