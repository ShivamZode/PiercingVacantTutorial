from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30, unique = True)
    password = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)

class UserLog(models.Model):
    username = models.CharField(max_length = 30, unique = True)
    password = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)

class Teacher(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class FaceData(models.Model):

    face_descriptor = models.TextField()
    name = models.CharField(max_length = 30, unique = True)

    def __str__(self):
        return self.name

class Presenty(models.Model):
    name = models.CharField(max_length = 30)
    subject = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
    # Define the combination of fields that should be unique
        unique_together = ('name', 'subject' , 'date')
    

    def __str__(self):
        return self.subject

