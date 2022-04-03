from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name = 'homePage'),
    path('^profile/', views.profile, name='profile'),
    path('^search/', views.search_results, name='search_results'),
    path('^new/image$', views.new_image, name='newImage'),
    path('^image/',views.image,name ='image'),
    path('^like/', views.like_image, name='like-image'),
    path('^comment/', views.comment, name='comment'),
   
]