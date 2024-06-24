# portfolio/models.py

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    expertise_level = models.CharField(max_length=50, default='Beginner')
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(default='https://example.com') 
    image = models.ImageField(upload_to='project_images/', default='default.jpg') 

    
    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    
    def __str__(self):
        return self.degree
