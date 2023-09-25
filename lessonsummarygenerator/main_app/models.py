from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=100, blank = False)
    description = models.TextField(max_length=250, blank = False)
    keywords = ArrayField(models.CharField(max_length=100), blank = True)  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'concept_id': self.id})
    