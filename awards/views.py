from django.shortcuts import render


'''welcome view to process landing page'''
def welcome(request):
    projects = Project.objects.all()
    developers = Profile.objects.all()
    number = random.randrange(10)
    return render(request, 'home.html', {"projects":projects, "developers": developers, "random":number})

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        projects = Project.objects.all()
    except:
        raise Http404()
    return render(request, "single_project.html", {"project":project, "projects":projects})
