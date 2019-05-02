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
        x = self.profile_fname + " " + self.profile_lname
        return x

class Pet(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_species = models.CharField(max_length=20)
    pet_breed = models.CharField(max_length=20)
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_image = models.ImageField(upload_to='pet-pics')
    
    def __str__(self):
        x = self.pet_name + " the " + self.pet_breed + " " + self.pet_species
        return x
