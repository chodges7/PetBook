from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

from . import models
from . import forms

#@login_required(login_url="/login/")
#def index(request):
#    return HttpResponse("Hello World")

@login_required(redirect_field_name='/', login_url="/login/")
def index(request):
    context = {
        "body":"PetBook Template Variable",
        "title":"PetBook Hello"
    }
    return render(request, "page.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)
