from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ProfileForm(forms.Form):
    profile_bio = forms.CharField(label='Your Bio', max_length=500)
    profile_fname = forms.CharField(label='Your first name', max_length=50)
    profile_lname = forms.CharField(label='Your last name', max_length=50)

class PetForm(forms.Form):
    pet_name = forms.CharField(label="Your pet's name", max_length=50)
    pet_species = forms.CharField(label="Your pet's species", max_length=20)
    pet_breed = forms.CharField(label="Your pet's breed", max_length=20)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
