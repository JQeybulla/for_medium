from unicodedata import name
from django.urls import path
from .views import PersonList, ProjectList, NewsList, projects_and_news


urlpatterns = [
    path("projects/", ProjectList.as_view(), name="projects"),
    path("news/", NewsList.as_view(), name="news"),
    path("projects-news/", projects_and_news, name='projects_news'),
    path("persons/", PersonList.as_view(), name="persons"),
]
