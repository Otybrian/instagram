from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import instaclone

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    caption= models.TextField(max_length=300)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    comments= models.IntegerField(default=0)
    likes_counter=models.IntegerField(default=0)
    like= models.ManyToManyField(User,default=None,blank=True,related_name='like')


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self,caption):
        self.caption = caption
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        instaclone = cls.objects.filter(name__icontains=search_term)
        return instaclone

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=300,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

class Likes(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow' 
