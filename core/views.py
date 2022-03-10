from django.shortcuts import render
from .models import Project, News
from rest_framework.generics import ListAPIView
from .serializers import ProjectSerializer, NewstSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class ProjectList(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class NewsList(ListAPIView):
    serializer_class = NewstSerializer
    queryset = News.objects.all()


@api_view(['GET'])
def projects_and_news(request):
    if request.method == 'GET':

        # first we get the querysets
        projects = Project.objects.all()
        news = News.objects.all()

        # then we serializer the data
        projects_serializer = ProjectSerializer(projects, many=True, context={'request': request})
        news_serializer = NewstSerializer(news, many=True, context={'request': request})

        print(projects_serializer.data)
        # print(news_serializer)

        data = projects_serializer.data + news_serializer.data

        return Response(data)
