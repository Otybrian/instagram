from django.test import TestCase
from .models import Profile, Post
from django.contrib.auth.models import User
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='charles')
        self.user.save()
