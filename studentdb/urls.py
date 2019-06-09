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
from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.StudentBatch1List.as_view(), name = "form1"),
    path('2/', views.StudentBatch2List.as_view(), name = "form2"),
    path('3/', views.StudentBatch3List.as_view(), name = "form3"),
    path('4/', views.StudentBatch4List.as_view(), name = "form4"),
    path('5/', views.StudentBatch5List.as_view(), name = "form5"),
    path('', views.StudentList.as_view(), name = 'studentdb_index'),
    path('1/<pk>/', views.StudentDetail.as_view(), name = "studentdetail"),
    path('2/<pk>/', views.StudentDetail.as_view(), name = "studentdetail"),
    path('3/<pk>/', views.StudentDetail.as_view(), name = "studentdetail"),
    path('4/<pk>/', views.StudentDetail.as_view(), name = "studentdetail"),
    path('5/<pk>/', views.StudentDetail.as_view(), name = "studentdetail"),
    path('<pk>/', views.StudentDetail.as_view(), name = "studentdetail"),


]
