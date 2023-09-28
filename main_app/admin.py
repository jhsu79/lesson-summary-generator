from django.contrib import admin
from .models import Concept, Student, LessonNote

# Register your models here.
admin.site.register(Concept)
admin.site.register(Student)
admin.site.register(LessonNote)