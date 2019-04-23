
# IF YOU AUTO INDENT MAKE SURE RETURN IS CORRECTED ON LAST LINE

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from . import models
from . import forms

# Chat system views from bit.ly/herokuDjangoChatSystem

import random
import string
from haikunator import Haikunator
from django.db import transaction

haikunator = Haikunator()

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def about(request):
    return render(request, "chat/about.html")

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def new_room(request):
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()
            if models.Room.objects.filter(label=label).exists():
                continue
            new_room = models.Room.objects.create(label=label)
    return redirect(chat_room, label=label)

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def chat_room(request, label):
    room, created = models.Room.objects.get_or_create(label=label)

    # Show the last 50 messages
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chat/room.html", {
        'room':room,
        'messages':messages,
        })

# Create your views here.

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def index(request):
    return redirect("/profile_page/")

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def profile_page(request):
    prof = models.Profile.objects.get(profile_user=request.user)
    context = {
            "body":"Welcome to your profile page",
            "title":"Profile page",
            "bio":prof.profile_bio,
            }
    return render(request, "profile_page.html", context=context)

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def pet_reg(request):
    if request.method == "POST":
        form_instance = forms.PetForm(request.POST)
        if form_instance.is_valid():
            new_pro = models.Pet()
            new_pro.pet_name = form_instance.cleaned_data["pet_name"]
            new_pro.pet_species = form_instance.cleaned_data["pet_species"]
            new_pro.pet_breed = form_instance.cleaned_data["pet_breed"]
            new_pro.pet_owner = request.user
            new_pro.save()
            form_instance = forms.PetForm()
            return redirect("/profile_page/")
    else:
        form_instance = forms.PetForm()
    context = {
            "form":form_instance,
            }
    return render(request, "registration/pet_reg.html", context=context)

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
            "form":form_instance,
            }
    return render(request, "registration/register.html", context=context)

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def pets_json(request):
    i_list = models.Pet.objects.filter(pet_owner=request.user)
    resp_list = {}
    resp_list["pets"] = []
    for item in i_list:
        prof = models.Profile.objects.get(profile_user=item.pet_owner)
        resp_list["pets"] += [{
            "pet":item.pet_name,
            "species":item.pet_species,
            "id":item.id,
            "breed":item.pet_breed,
            "owner":prof.profile_fname}]
    return JsonResponse(resp_list)
