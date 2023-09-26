from django.forms import ModelForm
from .models import LessonNote, Student

class LessonNoteForm(ModelForm):
  class Meta:
    model = LessonNote
    fields = '__all__'
    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)
        super(LessonNoteForm, self).__init__(*args, **kwargs)
        if student:
            self.fields['student'].queryset = Student.objects.filter(id=student.id)