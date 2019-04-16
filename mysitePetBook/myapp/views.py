from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

from . import models
from . import forms

@login_required(redirect_field_name='/', login_url="/login/")
def index(request):
    #profileList = models.Profile.objects.all()
    #for i in profileList:
    #    if request.User == profileList[i].Profile_user:
    #        profile_int = profileList[i]
    #profile_int = request.User.Profile
    context = {
        "body":"PetBook Template Variable",
        "title":"PetBook Hello",
        #"profile":profile_int
    }
    return render(request, "page.html", context=context)

@login_required(redirect_field_name='/', login_url="/login/")
def profile_reg(request):
    if request.method == "POST":
        form_instance = forms.ProfileForm(request.POST)
        if form_instance.is_valid():
            group = Group.objects.get(name='Has Profiles')
            new_pro = models.Profile()
            new_pro.profile_fname = form_instance.cleaned_data["profile_fname"]
            new_pro.profile_lname = form_instance.cleaned_data["profile_lname"]
            new_pro.profile_bio = form_instance.cleaned_data["profile_bio"]
            new_pro.profile_user = request.user
            new_pro.save()
            request.user.groups.add(group)
            form_instance = forms.ProfileForm()
            return redirect("/")
    else:
        form_instance = forms.ProfileForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/profile_reg.html", context=context)

@login_required(redirect_field_name='/', login_url="/login/")
def pet_reg(request):
    if request.method == "POST":
        form_instance = forms.PetForm(request.POST)
        if form_instance.is_valid():
            group = Group.objects.get(name='Has Profiles')
            new_pro = models.Profile()
            new_pro.profile_fname = form_instance.cleaned_data["profile_fname"]
            new_pro.profile_lname = form_instance.cleaned_data["profile_lname"]
            new_pro.profile_bio = form_instance.cleaned_data["profile_bio"]
            new_pro.profile_user = request.user
            new_pro.save()
            request.user.groups.add(group)
            form_instance = forms.ProfileForm()
            return redirect("/")
    else:
        form_instance = forms.ProfileForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/profile_reg.html", context=context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    request.user = authenticate(request, username=username, password=password)
    if request.user is not None:
        login(request, request.user)
        return redirect("/")
    else:
        return redirect("/login/")

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/profile_reg/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)

def pets_json(request):
    i_list = models.Pet.objects.all()
    resp_list = {}
    resp_list["pets"] = []
    for item in i_list:
        resp_list["pets"] += [{
            "pet":item.pet_name,
            "species":item.pet_species,
            "id":item.id,
            "breed":item.pet_breed,
            "owner":item.pet_owner,
        }]
    return JsonResponse(resp_list)
