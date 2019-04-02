from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ProfileForm(forms.Form):
    Profile_Bio



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
