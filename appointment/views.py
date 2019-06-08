import datetime
from django.views import View
from django.shortcuts import render, redirect
from .models import Appointment
from django.core import serializers
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.forms import modelformset_factory
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required, user_passes_test

#test to see if User is a counselour
def is_counselour(user):
    return user.groups.filter(name='Counselour').exists()

def table(request, year, month, day):
    appointments = serializers.serialize('json', Appointment.objects.filter(start_time__year=year, 
                                                            start_time__month=month, 
                                                            start_time__day=day,
                                                            approval=True),
                                                        fields=('objective', 
                                                                'start_time', 
                                                                'end_time',
                                                                'client',
                                                                'rooom'))    
    return render(request,'table.html',context={"appointments" : appointments,
                                                })


#detail view generic
class AppointmentDetailView(DetailView):

    model = Appointment


#forms for appointment
@login_required
def appointment_new(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user
            month = appointment.start_time.month
            day = appointment.start_time.day
            year = appointment.start_time.year
            appointment.save()
            return redirect('/appointment/view/' + str(month) + '/' + str(day) + '/' + str(year))
    else:
        form = AppointmentForm()
    return render(request, "form.html", {'form': form})

#user appointment request inbox and outbox
@login_required
def appointment_admin(request):
    if is_counselour(request.user):
        AppointmentFormSet = modelformset_factory(Appointment, fields=('objective','start_time','end_time','client','rooom','approval'),extra=0)

        if request.method == 'POST':
            form = AppointmentFormSet(request.POST)
            instances = form.save(commit=False)

            for instance in instances:
                instance.save()

        form = AppointmentFormSet

        return render(request, 'appointment_admin.html', { 'form' : form ,
                                                        'user' : request.user})
    else:
        return redirect('list/')

from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AppointmentListView(ListView):
    model = Appointment

    def get_queryset(self):
        queryset = super(AppointmentListView, self).get_queryset()
        queryset = queryset.filter(client=self.request.user)
        return queryset

    #def post(self, request, *args, **kwargs):
    #    ids = self.request.POST.get('ids', "")
    #    # ids if string like "1,2,3,4"
    #    ids = ids.split(",")
    #    try:
    #        # Check ids are valid numbers
    #        ids = map(int, ids)
    #    except ValueError as e:
    #        return JsonResponse(status=400)
    #    # delete items
    #    self.model.objects.filter(id__in=ids).delete()
    #    return JsonResponse({"status": "ok"}, status=204)