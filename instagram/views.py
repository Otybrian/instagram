from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Image,Profile,Likes,Comment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, CommentForm, ProfileForm
from django.http  import Http404




# Create your views here.
def home(request):
    return render(request, 'home.html')
