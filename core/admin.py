import imp
from django.contrib import admin
from .models import Project, News

# Register your models here.

admin.site.register(Project)
admin.site.register(News)
