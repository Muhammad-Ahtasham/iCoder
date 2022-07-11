from home import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('signup', views.handleSignUp, name='handleSignUp'),
    path('login', views.handleLogIn, name='handleLogIn'),
    path('logout', views.handleLogOut, name='handleLogOut'),
    path('search', views.search, name='search')
]