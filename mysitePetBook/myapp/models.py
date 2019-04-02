from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_fname = models.CharField(max_length=50)
    profile_lname = models.CharField(max_length=50)
    profile_bio = models.CharField(max_length=500)

    #def __str__(self):
    #    return 

class Pet(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_species = models.CharField(max_length=20)
    pet_breed = models.CharField(max_length=20)
    pet_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self);
        return self.pet_name
