from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name = 'homePage'),
    path(r'^profile/', views.profile, name='profile'),
    path(r'^search/', views.search_results, name='search_results'),
    path(r'^new/image$', views.new_image, name='newImage'),
    path(r'^image/',views.image,name ='image'),
    path(r'^like/', views.like_image, name='like-image'),
    path(r'^comment/', views.comment, name='comment'),
   
]