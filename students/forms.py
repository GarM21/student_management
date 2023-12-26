# students/forms.py
from django import forms
from .models import Student
from .models import Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'score']

class GradeDeleteForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = []

