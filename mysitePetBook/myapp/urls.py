from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index),
    path('edit/', views.edit),
    path('pets/', views.pets_json),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('pet_reg/', views.pet_reg),
    path('edit_bio/', views.edit_bio),
    path('register/', views.register),
    path('profile_page/', views.profile_page),
]
