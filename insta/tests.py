from django.test import TestCase
from .models import Profile,Image

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.bio = []
