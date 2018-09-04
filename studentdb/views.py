from django.shortcuts import render
from .models import Student
from django.views.generic import ListView, DetailView
# Create your views here.

#def studentdb_home(request):
#    student = Student
#    return render(request, 'studentdb/homepage.html', context = {'student' : student })

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student
