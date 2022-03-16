from operator import mod
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    profession = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name
