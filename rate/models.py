from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    '''
    class to create user profile
    '''
    profile_photo = models.ImageField(upload_to = 'pictures')
    bio = models.TextField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
