import imp
from django.contrib import admin
from .models import Project, News, Person
from modeltranslation.admin import TranslationAdmin

# Register your models here.

admin.site.register(Project)
admin.site.register(News)

# admin.site.register(Person)


class PersonAdmin(TranslationAdmin):
    pass

admin.site.register(Person, PersonAdmin)
