from django.db import models
from django.contrib.auth.models import User

#https://www.webforefront.com/django/modeldatatypesandvalidation.html

class Album(models.Model):
    album_name          = models.CharField(max_length=1000)
    album_created_at    = models.DateTimeField(auto_now_add=True)
    user                = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

class Picture(models.Model):
    picture_file_name    = models.CharField(max_length=1000)
    picture              = models.ImageField(null=True, blank=True)
    picture_added_at     = models.DateTimeField(auto_now_add=True)
    album_id             = models.ForeignKey(Album, null=True, blank=True, on_delete=models.SET_NULL)
    user                 = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

class Folder(models.Model):
    folder_name          = models.CharField(max_length=1000)
    folder_created_at    = models.DateTimeField(auto_now_add=True)
    user                = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

class File(models.Model):
    file_file_name      = models.CharField(max_length=1000)
    file                = models.FileField(null=True, blank=True)
    file_added_at       = models.DateTimeField(auto_now_add=True)
    folder_id           = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.SET_NULL)
    user                = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
