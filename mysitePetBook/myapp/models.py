from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_fname = models.CharField(max_length=50)
    profile_lname = models.CharField(max_length=50)
    profile_bio = models.CharField(max_length=500)
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile-pics')

    def __str__(self):
        name = self.profile_fname + " " + self.profile_lname
        return name

class Pet(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_species = models.CharField(max_length=20)
    pet_breed = models.CharField(max_length=20)
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_image = models.ImageField(upload_to='pet-pics')

    def __str__(self):
        name = self.pet_name + " the " + self.pet_breed + " " + self.pet_species
        return name

#https://stackoverflow.com/questions/4564760/best-way-to-make-djangos-user-system-have-friends
class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friend_set", on_delete=models.CASCADE)

    def __str__(self):
        name = self.creator.get_username() + " friended " + self.friend.get_username()
        return name
