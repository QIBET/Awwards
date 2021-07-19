from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.fields import DateField
from django.utils import timezone 
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    '''
    class to create user profile
    '''
    image = cloudinary.models.CloudinaryField('image',null=True, blank=True)    
    bio = models.TextField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        
        return self.profile_photo
    
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
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    project_name = models.CharField(max_length=30)
    description = models.TextField()
    livesite = models.URLField()
    image = cloudinary.models.CloudinaryField('image',null=True, blank=True)
    date_posted = models.DateField(default=timezone.now)
   

    def __str__(self):
        
        return self.project_name
    
    def save_project(self):
        '''
        method to save instances of projects
        '''
        self.save()

    def delete_project(self):
        '''
        method to delete instances of projects
        '''
        self.delete()

    @classmethod
    def get_projects(cls):
        '''
        method to return all projects
        '''
        all_projects = cls.objects.all()

        return all_projects

    @classmethod
    def search_by_project_name(cls,search_term):
        '''
        method to search and return project by name
        '''
        project = cls.objects.filter(project_name__icontains=search_term)
        return project


    