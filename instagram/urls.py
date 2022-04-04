from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name = 'homePage'),
    path('newprofile/', views.addProfile, name='newprofile'),
    path('profile/', views.userProfile, name='profile'),
    path('search/', views.search_results, name='search_results'),
    path('newimage/', views.newImage, name='newImage'),
    path('image/',views.image,name ='image'),
    re_path('like/', views.likeImage, name='like-image'),
    re_path('comment/', views.postComment, name='comment'),
   
]