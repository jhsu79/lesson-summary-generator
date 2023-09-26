from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from enum import Enum, auto

class PROGRAM_CHOICES(Enum):
    TUTORING = '1-on-1'
    GROUP = 'Small Group' 
    CLASS = 'Classroom'
    

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=100, blank = False)
    description = models.TextField(max_length=250, blank = False)
    keywords = ArrayField(models.CharField(max_length=100), blank = True)  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'concept_id': self.id})

class Student(models.Model):
    first_name = models.CharField(max_length=50, blank = False)
    last_name = models.CharField(max_length=50, blank = False)
    pronouns = models.CharField(blank = False)
    program_type= models.CharField(max_length=15, choices=[(choice.value, choice.name) for choice in PROGRAM_CHOICES], )  
    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'student_id': self.id})