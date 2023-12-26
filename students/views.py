# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Grade
from .forms import StudentForm
from .forms import GradeForm, GradeDeleteForm

def home(request):
    students = Student.objects.all()
    return render(request, 'students/home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Перенаправление на страницу со списком студентов
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    grades = Grade.objects.filter(student=student)
    average_grade = student.calculate_average_grade()
    return render(request, 'students/student_detail.html', {'student': student, 'grades': grades, 'average_grade': average_grade})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            student_id = form.cleaned_data['student'].id
            grade.student_id = student_id
            grade.save()
            return redirect('student_detail', student_id=student_id)
    else:
        form = GradeForm()

    return render(request, 'students/add_grade.html', {'form': form})


def delete_grade(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        form = GradeDeleteForm(request.POST, instance=grade)
        if form.is_valid():
            grade.delete()
            return redirect('student_detail', student_id=grade.student.id)
    else:
        form = GradeDeleteForm(instance=grade)

    return render(request, 'students/delete_grade.html', {'form': form, 'grade': grade})