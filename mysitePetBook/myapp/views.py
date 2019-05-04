
# IF YOU AUTO INDENT MAKE SURE RETURN IS CORRECTED ON LAST LINE

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

from . import models
from . import forms

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def index(request):
    return redirect("/profile_page/")

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def profile_page(request):
    prof = models.Profile.objects.get(profile_user=request.user)
    welc = "Welcome to your profile page: "
    welc += prof.profile_fname + " " + prof.profile_lname
    if request.method == "POST":
        form = forms.BioForm(request.POST)
        if form.is_valid():
            prof.profile_bio = form.cleaned_data["profile_bio"]
            prof.save()
            return redirect("/")
    else:
        form = forms.BioForm()
    context = {
        "body":welc,
        "form":form,
        "title":"Profile page",
        "bio":prof.profile_bio,
        "profile_picture":prof.profile_image.url,
        }
    return render(request, "profile_page.html", context=context)

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def edit(request):
    prof = models.Profile.objects.get(profile_user=request.user)
    if request.method == "POST":
        form_instance = forms.ProfileForm(request.POST, request.FILES)
        if form_instance.is_valid():
            prof.profile_image = form_instance.cleaned_data["profile_image"]
            prof.profile_fname = form_instance.cleaned_data["profile_fname"]
            prof.profile_lname = form_instance.cleaned_data["profile_lname"]
            prof.profile_bio = form_instance.cleaned_data["profile_bio"]
            prof.save()
            return redirect("/")
    else:
        form_instance = forms.ProfileForm()

    context = {
        "form":form_instance,
        "prof":prof,
        "title":"Editing profile"
        }
    return render(request, "registration/edit.html", context=context)

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def pet_reg(request):
    if request.method == "POST":
        form_instance = forms.PetForm(request.POST, request.FILES)
        if form_instance.is_valid():
            new_pet = models.Pet()
            new_pet.pet_owner = request.user
            new_pet.pet_name = form_instance.cleaned_data["pet_name"]
            new_pet.pet_image = form_instance.cleaned_data["pet_image"]
            new_pet.pet_breed = form_instance.cleaned_data["pet_breed"]
            new_pet.pet_species = form_instance.cleaned_data["pet_species"]
            new_pet.save()
            form_instance = forms.PetForm()
            return redirect("/profile_page/")
    else:
        form_instance = forms.PetForm()
    context = {
        "form":form_instance,
        "title":"Pet Registration"
        }
    return render(request, "registration/pet_reg.html", context=context)

@login_required(redirect_field_name='/profile_page/', login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
        "title":"Registering User",
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
            "image":item.pet_image.url,
            "breed":item.pet_breed,
            "owner":prof.profile_fname}]
    return JsonResponse(resp_list)
