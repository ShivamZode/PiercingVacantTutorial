from django.db import models
from profiles.models import Profile
import datetime


# Create your models here.
# we are creating this model to store the accuracy of the facial scan, if the some user accidentally logs in to the other users profile , we compare the phto and the bio of the user 
#class Log is in many to one relationship with profiles 
class Log(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'logs')
    is_correct = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Log of {self.profile.id}'
