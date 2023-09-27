from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from enum import Enum, auto


class PROGRAM_CHOICES(Enum):
    TUTORING = "1-on-1"
    GROUP = "Small Group"
    CLASS = "Classroom"

class HOMEWORK_COMPLETION_CHOICES(Enum): 
    NONE = 'None'
    SOME = 'Less than 50%'
    HALF = '50%'
    MOST = 'Greater than 50%'
    ALL =  '100%'

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=250, blank=False)
    keywords = ArrayField(models.CharField(max_length=100), blank=True)
    def __str__(self): 
        return f"{self.name}"
    def get_absolute_url(self):
        return reverse("detail", kwargs={"concept_id": self.id})


class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    pronouns = models.CharField(blank=False)
    program_type = models.CharField(
        max_length=15,
        choices=[(choice.value, choice.name) for choice in PROGRAM_CHOICES],
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return f"{self.first_name} {self.last_name}"
    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"student_id": self.id})


class LessonNote(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField("Lesson Date")
    homework_completion_level = models.CharField(
        max_length=16,
        choices=[(choice.value, choice.name) for choice in HOMEWORK_COMPLETION_CHOICES],
    )
    homework_accuracy_level = models.CharField(max_length=16, blank=False)
    homework_review_comments = models.TextField(max_length=250, blank=False)
    concepts_covered = models.ManyToManyField(Concept, blank=True)
    lesson_comments = models.TextField(max_length=250, blank=False)
    homework_assigned = models.BooleanField(default=True)
    assigned_homework = models.TextField(max_length=250, blank=False)
    next_lesson_date = models.DateField("Next Lesson Date")
    private_notes = models.TextField(blank=False)
    lesson_summary = models.TextField(max_length=500, blank=True)

    def __str__(self):
        concepts = ", ".join(concept.name for concept in self.concepts_covered.all())
        student_name = f"{self.student.first_name} {self.student.last_name}"
        return f"Lesson Note for Student: {student_name} on {self.date}. Concepts Covered: {concepts}"
    def get_absolute_url(self):
        return reverse("lesson_note_detail", kwargs={"student_id": self.student.id, "lesson_note_id": self.id})
