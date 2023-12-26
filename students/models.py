# students/models.py
from django.db import models
from django import forms

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def calculate_average_grade(self):
        grades = self.grade_set.all()
        if grades:
            total_score = sum(grade.score for grade in grades)
            return total_score / len(grades)
        return 0.0

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.score}"
