from django.contrib import admin
from django.urls import path, include
from home import views
from . import views

urlpatterns = [ 
   path('', views.home, name='home'),
   path('about', views.about, name='about'),
   path('contact', views.contact, name="contact"),
   path('services', views.services, name="contact"),
   path('faq', views.faq, name="contact"),
   path('team', views.team, name="contact"),
   path('signup', views.handleSignup, name='handleSignup'),
   path('login', views.handleLogin, name='handleLogin'),
   path('logout/', views.handleLogout, name='handleLogout'),
]