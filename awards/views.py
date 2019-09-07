from django.shortcuts import render


'''welcome view to process landing page'''
def welcome(request):
    projects = Project.objects.all()
    developers = Profile.objects.all()
    number = random.randrange(10)
    return render(request, 'home.html', {"projects":projects, "developers": developers, "random":number})

