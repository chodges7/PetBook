
# IF YOU AUTO INDENT MAKE SURE RETURN IS CORRECTED ON LAST LINE

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

from . import models
from . import forms

@login_required(login_url="/login/")
def index(request):
    return redirect("/profile_page/")

@login_required(login_url="/login/")
def home(request):
    prof = models.Profile.objects.get(profile_user=request.user)
    welc = "Welcome to the homepage: "
    welc += prof.profile_fname + " " + prof.profile_lname
    if request.method == "POST":
        form = forms.StatusForm(request.POST, request.FILES)
        if form.is_valid():
            new_status = models.Status()
            new_status.status_field = form.cleaned_data["status_field"]
            new_status.status_image = form.cleaned_data["status_image"]
            new_status.status_author = request.user
            new_status.save()
            form = forms.StatusForm()
            return redirect("/home/")
    else:
        form = forms.StatusForm()
    context = {
        "body":welc,
        "form":form,
        "title":"Homepage",
        "comm_form":forms.CommentForm(),
        }
    return render(request, "homepage.html", context=context)

@login_required(login_url="/login/")
def comment_view(request, sug):
    if request.method == "POST":
        form_instance = forms.CommentForm(request.POST)
        if form_instance.is_valid():
            sug_instance = models.Status.objects.get(id=sug)
            new_comm = models.Comment()
            new_comm.comment_field = form_instance.cleaned_data["comment_field"]
            new_comm.comment_status = sug_instance
            new_comm.comment_author = request.user
            new_comm.save()
            return redirect("/home/")
    else:
        form_instance = forms.CommentForm()
    context = {
        "body":"Hello World Template Variable",
        "title":"Commenting",
        "form":form_instance,
        "suggestion":sug,
    }
    return render(request, "comment.html", context=context)

@login_required(login_url="/login/")
def profile_page(request):
    prof = models.Profile.objects.get(profile_user=request.user)
    welc = "Welcome to your profile page: "
    welc += prof.profile_fname + " " + prof.profile_lname
    if request.method == "POST":
        form = forms.BioForm(request.POST)
        if form.is_valid():
            prof.profile_bio = form.cleaned_data["profile_bio"]
            prof.save()
            form = forms.BioForm()
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

@login_required(login_url="/login/")
def specific_profile(request, person):
    #Grab user model from person argument
    personUser = models.User.objects.get(username=person)
    #Then grab prof model from that user
    prof = models.Profile.objects.get(profile_user=personUser)
    welc = "Welcome to the profile page of: "
    welc += prof.profile_fname + " " + prof.profile_lname
    title = person + "'s profile page"
    theirPets = models.Pet.objects.filter(pet_owner=personUser)
    theirFriends = models.Friendship.objects.filter(creator=personUser)
    chat = "/chat/" + request.user.username + "-" + person
    context = {
        "chat":chat,
        "body":welc,
        "title":title,
        "theirPets":theirPets,
        "bio":prof.profile_bio,
        "theirFriends":theirFriends,
        "profile_picture":prof.profile_image.url,
        }
    return render(request, "specific_profile.html", context=context)


@login_required(login_url="/login/")
def new_friend(request):
    if request.method == "POST":
        form = forms.FriendForm(request.POST)
        if form.is_valid():
            new_friendship = models.Friendship()
            friend = form.cleaned_data["friend"]
            friend_user = models.User.objects.get(username=friend)
            if friend == friend_user.get_username():
                new_friendship.friend = friend_user
                new_friendship.creator = request.user
                new_friendship.save()
                return redirect("/")
    else:
        form = forms.FriendForm()
    context = {
            "form":form,
            "title":"Making a new Friend"
            }
    return render(request, "registration/friend.html", context=context)

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def status_json(request):
    i_list = models.Status.objects.all()
    resp_list = {}
    resp_list["statuses"] = []
    for item in i_list:
        comments_list = []
        comm_list = models.Comment.objects.filter(comment_status=item)
        for comm in comm_list:
            comments_list += [{
                "comment":comm.comment_field,
                "author":comm.comment_author.username,
                "id":comm.id,
                "created_on":comm.created_on
            }]
        resp_list["statuses"] += [{
            "status":item.status_field,
            "author":item.status_author.username,
            "id":item.id,
            "comments":comments_list,
            "image":item.status_image.url,
            "crated_on":item.crated_on,
            "num_comments":len(comments_list)}]
    return JsonResponse(resp_list)

@login_required(login_url="/login/")
def friends_json(request):
    i_list = models.Friendship.objects.filter(creator=request.user)
    resp_list = {}
    resp_list["friends"] = []
    for item in i_list:
        accepted = False
        j_list = models.Friendship.objects.filter(creator=item.friend)
        for todo in j_list:
            if todo.friend == item.creator:
                accepted = True
        prof = models.Profile.objects.get(profile_user=item.friend)
        resp_list["friends"] += [{
            "id":item.id,
            "image":prof.profile_image.url,
            "friend":item.friend.get_username(),
            "creator":item.creator.get_username(),
            "created":item.created,
            "accepted":accepted}]
            
    return JsonResponse(resp_list)

@login_required(login_url="/login/")
def friends_json_slug(request, person):
    personUser = models.User.objects.get(username=person)
    i_list = models.Friendship.objects.filter(creator=personUser)
    resp_list = {}
    resp_list["friends"] = []
    for item in i_list:
        prof = models.Profile.objects.get(profile_user=item.friend)
        resp_list["friends"] += [{
            "id":item.id,
            "image":prof.profile_image.url,
            "friend":item.friend.get_username(),
            "created":item.created}]
    return JsonResponse(resp_list)

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def pets_json_slug(request, person):
    personUser = models.User.objects.get(username=person)
    i_list = models.Pet.objects.filter(pet_owner=personUser)
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
