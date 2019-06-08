from django.urls import path
from . import views

urlpatterns = [
    path('admin', views.appointment_admin, name='appointment-admin'),
    path('list', views.AppointmentListView.as_view(), name='appointment-list'),
    path('list/', views.AppointmentListView.as_view(), name='appointment-list'),
    path('new', views.appointment_new, name='appointment-new'),
    path('<pk>', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('view/<pk>', views.AppointmentDetailView.as_view  (), name='appointment-detail'),
    path('view/<month>/<day>/<year>', views.table, name='appointment-table'),
    path('view/<month>/<day>/<year>/<pk>', views.AppointmentDetailView.as_view(), name='appointment-detail'),
]
