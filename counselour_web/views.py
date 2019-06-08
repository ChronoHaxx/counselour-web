from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('Welcome to my website')
    return render(request,'homepage.html')

def about(request):
    #return HttpResponse('About Us')
    return render(request,'about.html')

def uglysyamimi(request):
    #PORTFOLIO SYAMIMI FOR HER BIRTHDAY
    return render(request,'uglysyamimi.html')
