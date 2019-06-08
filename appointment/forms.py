import datetime
import pytz

from django.contrib.auth.models import User
from django import forms
from .models import Appointment
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

utc = pytz.UTC

class AppointmentForm(forms.ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data # individual field's clean methods have already been called
        data = cleaned_data.get('end_time')
        data2 = cleaned_data.get('start_time')

        # Check if a date is not in the past. 
        if data < datetime.datetime.now(pytz.utc):
            raise ValidationError(_('Invalid date - end time in past'))

        # Check if a date is in the allowed range (after start_time).
        if data < data2 :
            raise ValidationError(_('Invalid date - end time before start time'))

        # Check if a date is not in the past. 
        if data2 < datetime.datetime.now(pytz.utc):
            raise ValidationError(_('Invalid date - start time in past'))

        # Check if a date is in the allowed range (+2 weeks from today).
        if data2 > datetime.datetime.now(pytz.utc) + datetime.timedelta(weeks=2):
            raise ValidationError(_('Invalid date - start time more than 2 weeks ahead'))
        # Remember to always return the cleaned data.
        return cleaned_data

    class Meta:
        model = Appointment
        fields = ('objective', 'start_time', 'end_time', 'rooom')
        widgets = {
            'start_time': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
            }
        ),
        'end_time': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
            }
        ),
        }
        labels = {
            'objective': _('Objective'),
            'rooom': _('Room'),
            'start_time': _('From'),
            'end_time': _('Till'),
            'client': _('User'),
        }
        help_texts = {
            'objective': _('Must be below 80 characters'),
        }
        error_messages = {
            'objective': {
                'max_length': _("The objective is too long."),
            },
        }
