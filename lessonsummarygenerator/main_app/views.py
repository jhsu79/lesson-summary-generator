from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Concept, Student, LessonNote
from .forms import LessonNoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import LessonNoteForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView): 
    template_name = 'about.html'

@login_required
def concepts_index(request): 
    concepts = Concept.objects.all().order_by('name')
    return render(request, 'concepts/index.html', {'concepts': concepts})

@login_required
def concept_detail (request, concept_id):  
    concept = Concept.objects.get(id=concept_id) 
    return render(request, 'concepts/detail.html', {'concept': concept})

class ConceptCreate(LoginRequiredMixin,CreateView): 
    model = Concept 
    fields = '__all__'

class ConceptUpdate(LoginRequiredMixin,UpdateView):
    model = Concept 
    fields = '__all__'
 
class ConceptDelete(LoginRequiredMixin,DeleteView):
      model = Concept
      success_url = '/concepts'

@login_required
def students_index(request): 
    students = Student.objects.filter(user=request.user).order_by('last_name')
    return render(request, 'students/index.html', {'students':students})

@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    lesson_notes = LessonNote.objects.filter(student=student)
    return render(request, 'students/detail.html', {'Student': student, 'lesson_notes': lesson_notes})

class StudentCreate(LoginRequiredMixin,CreateView): 
    model = Student
    fields = '__all__'
    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)
    
class StudentUpdate(LoginRequiredMixin,UpdateView):
    model = Student
    fields = '__all__'
 
class StudentDelete(LoginRequiredMixin,DeleteView):
      model = Student
      success_url = '/students'

@login_required
def lesson_note_detail(request, lesson_note_id, student_id):
    lesson_note = LessonNote.objects.get(id=lesson_note_id)
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/lesson_note.html', {'Student': student,'lesson_note' : lesson_note})

class LessonNoteCreate(LoginRequiredMixin,CreateView): 
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

class LessonNoteUpdate(LoginRequiredMixin,UpdateView): 
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

class LessonNoteDelete(LoginRequiredMixin,DeleteView):
      model = LessonNote
      success_url = '/students'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
