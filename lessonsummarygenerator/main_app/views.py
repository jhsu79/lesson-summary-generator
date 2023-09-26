from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Concept, Student, LessonNote
from .forms import LessonNoteForm
# from .forms import LessonNoteForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView): 
    template_name = 'about.html'

def concepts_index(request): 
    concepts = Concept.objects.all().order_by('name')
    return render(request, 'concepts/index.html', {'concepts': concepts})

def concept_detail (request, concept_id):  
    concept = Concept.objects.get(id=concept_id) 
    return render(request, 'concepts/detail.html', {'concept': concept})

class ConceptCreate(CreateView): 
    model = Concept 
    fields = '__all__'

class ConceptUpdate(UpdateView):
    model = Concept 
    fields = '__all__'
 
class ConceptDelete(DeleteView):
      model = Concept
      success_url = '/concepts'

def students_index(request): 
    students = Student.objects.all().order_by('last_name')
    return render(request, 'students/index.html', {'students':students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    lesson_notes = LessonNote.objects.filter(student=student)
    return render(request, 'students/detail.html', {'Student': student, 'lesson_notes': lesson_notes})

class StudentCreate(CreateView): 
    model = Student
    fields = '__all__'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
 
class StudentDelete(DeleteView):
      model = Student
      success_url = '/students'

def lesson_note_detail(request, lesson_note_id, student_id):
    lesson_note = LessonNote.objects.get(id=lesson_note_id)
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/lesson_note.html', {'Student': student,'lesson_note' : lesson_note})

class LessonNoteCreate(CreateView): 
    model = LessonNote 
    form_class = LessonNoteForm
    template_name = 'main_app/lessonnote_form.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)   
        # Get the current student
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)       
        # Set the student for the form
        form.instance.student = student        
        # Restrict the queryset of the 'student' field to the current student
        form.fields['student'].queryset = Student.objects.filter(id=student.id)
        return form

class LessonNoteUpdate(UpdateView): 
    model = LessonNote 
    fields = '__all__'

class LessonNoteDelete(DeleteView):
      model = LessonNote
      success_url = 'students/<int:student_id>/'