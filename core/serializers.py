from dataclasses import field
from tkinter import NE
from rest_framework import serializers
from . models import Person, Project, News


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class NewstSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
