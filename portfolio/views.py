from django.shortcuts import render, get_object_or_404
from . models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/home.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {'project': project}
    return render(request, 'portfolio/project-detail.html', context)

def wendy_home(request):
    return render(request, 'portfolio/wendy-home.html', {})

def about(request):
    return render(request, 'portfolio/about.html', {})
    

