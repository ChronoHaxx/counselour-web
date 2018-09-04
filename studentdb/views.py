from django.shortcuts import render
from .models import Student
from django.views.generic import ListView, DetailView
# Create your views here.

#def studentdb_home(request):
#    student = Student
#    return render(request, 'studentdb/homepage.html', context = {'student' : student })

class StudentList(ListView,):
    model = Student


class StudentBatch1List(ListView):
    model = Student
    context_object_name = 'studentBatch_list'
    queryset = Student.objects.filter(batch='1')
    template_name = 'books/student_list.html'


class StudentBatch2List(ListView):
    model = Student
    context_object_name = 'studentBatch_list'
    queryset = Student.objects.filter(batch='2')
    template_name = 'books/student_list.html'


class StudentBatch3List(ListView):
    model = Student
    context_object_name = 'studentBatch_list'
    queryset = Student.objects.filter(batch='3')
    template_name = 'books/student_list.html'


class StudentBatch4List(ListView):
    model = Student
    context_object_name = 'studentBatch_list'
    queryset = Student.objects.filter(batch='4')
    template_name = 'books/student_list.html'


class StudentBatch5List(ListView):
    model = Student
    context_object_name = 'studentBatch_list'
    queryset = Student.objects.filter(batch='5')
    template_name = 'books/student_list.html'


class StudentDetail(DetailView):
    model = Student
