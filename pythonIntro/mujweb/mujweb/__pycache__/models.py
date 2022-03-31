from itertools import starmap
from tracemalloc import start
from turtle import title
from django.db import models

from pythonIntro.mujweb.gaflix.models import SEX_CHOICES

class Teacher (models.Model):
        name = models.CharField(max_length=255)

class Course (models.Model):
    title = models.models.CharField(max_length=255)
    start = models.DateTimeField()

SEX_MALE = 'male'
SEX_FEMALE = 'female'
SEX_OTHER = 'other'

SEX_CHOICES = (
        (SEX_MALE, 'Muž')
        (SEX_FEMALE, 'Žena')
        (SEX_OTHER, 'Ostatní')
)

class Actor(models.Model):
        name = models.CharField(max_length=255)