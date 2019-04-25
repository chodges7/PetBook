from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index),
    path('pets/', views.pets_json),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('pet_reg/', views.pet_reg),
    path('register/', views.register),
    path('profile_page/', views.profile_page),

    # URLs from bit.ly/herokuDjangoChatSystem
    url(r'^about/$',  views.about, name='about'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]
