from django.test import TestCase
from .models import Profile, Post
from django.contrib.auth.models import User
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='brian')
        self.user.save()

        self.profile = Profile(id=1, name='image', profile_picture='brian.jpg', bio='I am me',
            user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)
