from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Concept, Student, LessonNote
from .forms import LessonNoteForm
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv
from django.contrib.auth.mixins import LoginRequiredMixin
import openai, os
load_dotenv()

## All basic view functions start here 
# Created Custom Views for Home and About Views. 
class HomeView(TemplateView):
    template_name = 'home.html'

# Create Customviews for certain pages. 
class AboutView(TemplateView): 
    template_name = 'about.html'

## All Concept view functions here. 
#Will need a refactor into a class list view. 
@login_required
def concepts_index(request): 
    concepts = Concept.objects.all().order_by('name')
    return render(request, 'concepts/index.html', {'concepts': concepts})

#Will need a refactor into a class detail view. 
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

## All Student view functions start here. 
# Will need a refactor into a Class List View. 
@login_required
def students_index(request): 
    students = Student.objects.filter(user=request.user).order_by('last_name')
    return render(request, 'students/index.html', {'students':students})

#Will need a refactor into a Class List View. 
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

## All lesson note view function here. 

def lesson_note_detail(request, lesson_note_id, student_id):
    lesson_note = LessonNote.objects.get(id=lesson_note_id)
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/lesson_note.html', {'Student': student,'lesson_note' : lesson_note})

## All API call view function here. 
def summarize_lesson_note(lesson_note_text):
        openai.api_key= os.getenv('OPEN_AI_KEY')
        prompt = lesson_note_text 
        print({prompt})
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.6,
            max_tokens=2048,
        )
    
        summary = response.choices[0].text
        print (response.choices)
        return summary

 
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
        ## Check to see if the form is valid and save. 
    def form_valid(self, form):
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)       
        form.instance.student = student        
        response = super().form_valid(form)

        ##Create form cleaned fields. 
        homework_accuracy_level = form.cleaned_data['homework_accuracy_level']
        homework_completion_level = form.cleaned_data['homework_completion_level']
        homework_review_comments = form.cleaned_data['homework_review_comments']
        concepts_covered = form.cleaned_data['concepts_covered']
        lesson_comments = form.cleaned_data['lesson_comments']
        assigned_homework = form.cleaned_data['assigned_homework']
        next_lesson_date = form.cleaned_data['next_lesson_date']
        ## AI Prompt
        lesson_note_text =  f"Create a four paragraph summary addressed to {student}'s parents using the following structure: the first paragraph summarizes the {homework_accuracy_level}, {homework_completion_level}, and {homework_review_comments}, the second paragraph summarizes the {concepts_covered} and {lesson_comments}, the third paragraph creates an ordered list from the {assigned_homework}, and the fourth paragraph states the {next_lesson_date}"
        ## Call the API and Save the Summary
        summary = summarize_lesson_note(lesson_note_text)
        self.object.lesson_summary = summary
        self.object.save()
        return response

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

## All sign up views here.  

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

