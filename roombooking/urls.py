"""counselour_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

from django.views.generic import TemplateView

from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = [
#    path('', views.AgendaList.as_view()),
    path('', views.roombooking_home),
    path('home/', TemplateView.as_view(template_name="roombooking/homepage.html"),),
    path('schedule/', include('schedule.urls')),
    path('fullcalendar/', TemplateView.as_view(template_name="roombooking/fullcalendar.html"), name='fullcalendar'),
#    path(f'/{date}', views.roombooking_detail),
#    path('/booking', views.roombooking_booking),
#    path('/counselour', views.roombooking_counselour),
]
