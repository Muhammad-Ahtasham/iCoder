from blog import views
from django.urls import path

urlpatterns = [
     # API to post comments 
     path('postComment', views.postComment, name='postComment'),
     
     
     path('', views.blogHome, name='blogHome'),
     path('<str:slug>', views.blogPost, name='blogPost'),
]
