from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from django.forms.widgets import Textarea
from .models import Image,Profile,Comment

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date','comments','likes_counter','like']
        widgets = {
            'id':'form'
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']
        widgets = {
            'bio': Textarea(attrs={'cols': 30, 'rows': 3}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        
       