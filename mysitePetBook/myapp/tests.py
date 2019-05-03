from django.test import TestCase
from . import models

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        models.Profile.objects.create(profile_fname="first")
        models.Profile.objects.create(profile_lname="last")
        models.Profile.objects.create(profile_bio="bio")

    def test_profile_to_string(self):
        first = models.Profile.objects.get(profile_fname="first")
        last = models.Profile.objects.get(profile_lname="last")
        bio = models.Profile.objects.get(profile_bio="bio")
        self.assertEqual(str(first), 'first')
        self.assertEqual(str(last), 'last')
        self.assertEqual(str(bio), 'bio')

class PetTestCase(TestCase):
    def setUp(self):
        models.Pet.objects.create(pet_name="name")
        models.Pet.objects.create(pet_breed="breed")
        models.Pet.objects.create(pet_species="species")

    def test_profile_to_string(self):
        name = models.Pet.objects.get(pet_name="name")
        breed = models.Pet.objects.get(pet_breed="breed")
        species = models.Pet.objects.get(pet_species="species")
        self.assertEqual(str(name), 'name')
        self.assertEqual(str(breed), 'breed')
        self.assertEqual(str(species), 'species')
