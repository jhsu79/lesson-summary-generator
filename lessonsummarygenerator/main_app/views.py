from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView): 
    template_name = 'about.html'


concepts = [{'name': 'Intro to HTML', 'description': 'a basic lesson in how to build an html web page from scratch, understand the syntax and semantic elements of HTML, and correctly indent and nest html', 'keywords': ['HTML', 'Fundamentals', 'Syntax', 'Semantic' ,'fundamentals'], }, {'name': 'Intro to CSS', 'description': 'a basic lesson in how to style the elements on a web page, understand the css box model, and use css selectors to target elements for styling', 'keywords': ['box model', 'box-sizing', 'fundamentals', 'selectors', 'css']},{'name': 'Intro to Javascript', 'description':'An introduction to data types, variables, primitives in Javascript', 'keywords':['data types', 'primitives', 'javascript', 'fundamentals'],}]

def concepts_index(request): 
    return render(request, 'concepts/index.html', {'concepts': concepts})

def concept_detail (request, concept_id):  
    concept = concepts.get(id=concept_id) 
    return render(request, 'concepts/detail.html', {'concepts': concept})

# class ConceptsIndexView(ListView):  
#     model = Concept
#     def get_context_data(self, kwargs): 
#         context = super().get_context_data(**kwargs) 
#         return context