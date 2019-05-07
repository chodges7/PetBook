from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('edit/', views.edit),
    path('pets/', views.pets_json),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('pet_reg/', views.pet_reg),
    path('friends/', views.friends_json),
    path('statuses/', views.status_json),
    path('register/', views.register),
    path('new_friend/', views.new_friend),
    path('profile_page/', views.profile_page),
    path('comment/<int:sug>/', views.comment_view),
]
