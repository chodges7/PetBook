from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . import models

class ProfileForm(forms.Form):
    profile_bio = forms.CharField(label='Your new Bio', max_length=500)
    profile_fname = forms.CharField(label='Your corrected first name', max_length=50)
    profile_lname = forms.CharField(label='Your corrected last name', max_length=50)
    profile_image = forms.ImageField()

class BioForm(forms.Form):
    profile_bio = forms.CharField(label='Your new Bio', max_length=500)

class PetForm(forms.Form):
    pet_name = forms.CharField(label="Your pet's name", max_length=50)
    pet_species = forms.CharField(label="Your pet's species", max_length=20)
    pet_breed = forms.CharField(label="Your pet's breed", max_length=20)
    pet_image = forms.ImageField()

class FriendForm(forms.Form):
    friend = forms.CharField(validators=[friend_exists], label="Your new friend's username", max_length=50)

def friend_exists(value):
    friend = User.objects.filter(username=value)
    if friend.count()<=0:
        raise forms.ValidationError("Friend doesn't exist")
    return value

class StatusForm(forms.Form):
    status_image = forms.ImageField()
    status_field = forms.CharField(label="Your new status", max_length=240)

class CommentForm(forms.Form):
    comment_field = forms.CharField(label='Comment', max_length=240)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    profile_bio = forms.CharField(label='Your Bio', max_length=500)
    profile_fname = forms.CharField(label='Your first name', max_length=50)
    profile_lname = forms.CharField(label='Your last name', max_length=50)
    profile_image = forms.ImageField()

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            new_pro = models.Profile()
            new_pro.profile_user = user
            new_pro.profile_bio = self.cleaned_data["profile_bio"]
            new_pro.profile_fname = self.cleaned_data["profile_fname"]
            new_pro.profile_lname = self.cleaned_data["profile_lname"]
            new_pro.profile_image = self.cleaned_data["profile_image"]
            new_pro.save()
        return user
