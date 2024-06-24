# portfolio/views.py

from django.shortcuts import render
from .models import Skill, Project, Experience, Education

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()[:3]  # Show only 3 projects on home page
    context = {
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'home.html', context)

def about(request):
    experiences = Experience.objects.all()
    education = Education.objects.all()
    context = {
        'experiences': experiences,
        'education': education,
    }
    return render(request, 'about.html', context)

def projects(request):
    all_projects = Project.objects.all()  # Fetch all projects
    context = {
        'projects': all_projects,
    }
    return render(request, 'projects.html', context)

def contact(request):
    return render(request, 'contact.html')
