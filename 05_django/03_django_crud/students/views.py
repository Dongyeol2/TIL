from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()[::-1]
    context = {
        'students':students
    }
    return render(request,'students/index.html',context)

#사용자에게 게시글 작성 폼을 보여주는 함수
def new(request):
    return render(request,'students/new.html')

#사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')

    student = Student(name=name, age=age, email=email)
    student.save()
    
    return redirect('students:index')

#게시글 상세정보를 가져오는 함수
def detail(request,student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {
        'student':student
    }
    return render(request,'students/detail.html',context)
    
# 게시글 삭제 함수
def delete(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.delete()
    return redirect('students:index')

# 사용자에게 게시글 수정 폼을 던져주는 함수
def edit(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    context = {'student': student}
    return render(request, 'students/edit.html', context)

# 수정 사항을 받아서 DB에 저장(반영)하는 함수
def update(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.email = request.POST.get('email')
    student.save()
    return redirect('students:detail',student_pk)