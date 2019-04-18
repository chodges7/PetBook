from django.urls import path
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
]
