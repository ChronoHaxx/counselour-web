from django.http import HttpResponse
from django.shortcuts import render
from roombooking.models import Status

def homepage(request):
    status = Status
    #return HttpResponse('Welcome to my website')
    return render(request,'homepage.html',{'instance':status})

def about(request):
    #return HttpResponse('About Us')
    return render(request,'about.html')

def element(request):
    return render(request,'ui-elements.html')
