from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE


# Create your models here.
class Profile(models.Model):
    '''
    class to create user profile
    '''
    profile_photo = CloudinaryField('image', blank=True, null=True)
    bio = models.TextField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        
        return self.profile_photo.url
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    @classmethod   
    def update_bio(cls,id,new_bio):
        cls.objects.filter(pk = id).update(bio=new_bio)
        new_bio_object = cls.objects.get(bio = new_bio)
        new_bio = new_bio_object.bio
        return new_bio

class Projects(models.Model):
    '''
    class to create instances of projects
    '''
    project_name = models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey('User', on_delete = models.CASCADE,null='True', blank=True)
    livesite = models.URLField()
    image = CloudinaryField('image', blank=True, null=True)

    def save(self):
        '''
        method to save instances of projects
        '''
        self.save()

    def delete_project(self):
        '''
        method to delete instances of projects
        '''
        self.delete()

    