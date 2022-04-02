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


class TestPost(TestCase):
    def setUp(self):
        self.profile = Profile(name='brian', user=User(username='otieno'))
        self.profile.save()

        self.image = Post(image='brian.png', name='test', caption='test', user=self.profile)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image, Post))

    def test_save_image(self):
        self.image.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)
