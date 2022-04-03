from django.test import TestCase
from .models import Image


# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image=Image( image ='image.jpg',name= 'Myself', 
        caption ='some moments are not easy to relive',
        comments='5',likes_counter=10,likes=10)


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))   

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def tearDown(self):
        Image.objects.all().delete()
