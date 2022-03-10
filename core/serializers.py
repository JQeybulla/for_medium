from dataclasses import field
from tkinter import NE
from rest_framework import serializers
from . models import Project, News


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class NewstSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
