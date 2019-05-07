from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Friendship)
admin.site.register(models.Profile)
admin.site.register(models.Pet)
admin.site.register(models.Status)
admin.site.register(models.Comment)
