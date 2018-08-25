from django.shortcuts import render

# Create your views here.
def roombooking_home(request):
    return render(request, 'roombooking/homepage.html')
