from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index),
    path('pets/', views.pets_json),
    path('about/', views.about),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('pet_reg/', views.pet_reg),
    path('register/', views.register),
    path('new_room/', views.new_room),
    path('chat_room/', views.chat_room),
    path('profile_page/', views.profile_page),
]
