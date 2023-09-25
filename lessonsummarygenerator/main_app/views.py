from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Concept, Student
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

def student_detail (request, student_id):  
    student = Student.objects.get(id=student_id) 
    return render(request, 'students/detail.html', {'Student': student} )

class StudentCreate(CreateView): 
    model = Student
    fields = '__all__'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
 
class StudentDelete(DeleteView):
      model = Student
      success_url = '/students'