from django.shortcuts import render

# Create your views here.


def home(request):
    home = 'Welcome'
    return render(request, 'home.html', {'home':home})