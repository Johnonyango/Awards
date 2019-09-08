from django.contrib import admin
from django.contrib import admin
from .models import Project,Profile, AwardsProfiles, AwardsProjects, Rating

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(AwardsProfiles)
admin.site.register(AwardsProjects)
admin.site.register(Rating)