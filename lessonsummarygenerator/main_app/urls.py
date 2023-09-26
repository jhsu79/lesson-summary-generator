from django.urls import path
from . import views
from .views import HomeView, AboutView


urlpatterns = [
	path('', HomeView.as_view(), name = 'home'), 
    path('about/', AboutView.as_view(), name= 'about'),
    path('concepts/', views.concepts_index, name='concepts_index'),
    path('concepts/<int:concept_id>/', views.concept_detail, name='detail'),   
    path('concepts/create/', views.ConceptCreate.as_view(), name='concept_create'),
    path('concepts/<int:pk>/update/', views.ConceptUpdate.as_view(), name='concept_update'),
    path('concepts/<int:pk>/delete/', views.ConceptDelete.as_view(), name='concept_delete'),
    path('students/', views.students_index, name='students_index'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),   
    path('students/create/', views.StudentCreate.as_view(), name='student_create'),
    path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),
    path('students/<int:student_id>/lessons/<int:lesson_note_id>', views.lesson_note_detail, name='lesson_note_detail'),
    # path('students/<int:student_id>/lessons/create', views.LessonNoteCreate, name='lesson_note_create'),
    # path('students/<int:pk>/lessons/update/', views.LessonNoteUpdate.as_view(), name='student_update'),
    # path('students/<int:pk>/lessons/delete/', views.LessonNoteDelete.as_view(), name='student_delete'),
]    

 