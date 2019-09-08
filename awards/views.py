from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .models import Profile, Project, Rating
from .forms import NewRatingForm, NewProjectForm, NewProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework import status
from .permissions import IsAdminOrReadOnly
import datetime as dt
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



'''welcome view to process landing page'''
def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        projects = Project.objects.all()
    except:
        raise Http404()
    return render(request, "single_project.html", {"project":project, "projects":projects})


@login_required(login_url='/accounts/login/')
def index(request):
  id = request.user.id
  projects = Project.objects.all().order_by('-pub_date')

  return render(request, 'index.html',{'projects':projects,'profile':profile})

@login_required(login_url='/accounts/login/')
def myprojects(request):
    projects = Project.objects.all().order_by()
    return render(request,'myprojects.html', {'projects':projects})

@login_required(login_url='/accounts/login/')
def new_projects(request):
  ida = request.user.id

  if request.method == 'POST':
    form = NewProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.save()
    return redirect('index')

  else:
    form = NewProjectForm()

  return render(request, 'new_project.html',{'form':form,'profile':profile})