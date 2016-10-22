from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError
from django.db.models import Q
from django import forms
from .models import Booking
from datetime import timedelta
import datetime

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['Firstname', 'Surname', 'profile_pic', 'first_line_of_address',
                  'second_line_of_address', 'County', 'City', 'Postcode',
                  'Telephone_number']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



"""
This form is used for booking the hall for an event by registered users and the request will be sent to the admin only
if the timing slot is available for booking.
"""


class BookingForm(forms.ModelForm):
    # This connects the 'Booking' model with this form and shows the specified fields on the html.
    class Meta:
        model = Booking
        exclude = ['status', 'email']

    """
    If the input date is not valid then it will show a validation message.
    The form will also raise a validation error if the start time or the end time of the event is between the timings
    for	already booked or hall to be booked. e.g. If the hall is booked from 8AM to 10AM, then the user can't book
    the hall from 9AM to 10AM.
    """

    def clean(self):
        try:
            # Getting form data used for checking whether the booking can be done or not for filled entries.
            form_data = self.cleaned_data
            event_date = form_data['date']
            doc = form_data['doctor']
            event_start = form_data['start_time']
            print(event_start)


            # Getting the current date and time for comparing
            time_now = datetime.datetime.now().strftime('%H:%M:00')
            date_today = datetime.date.today()

            # For converting event_start from datetime.time to datetime.datetime, combine method is used for it and then
            # adding or subtracting number of hours from it.
            e_start = (datetime.datetime.combine(datetime.date.today(), event_start) + datetime.timedelta(minutes=1)) \
                .strftime('%H:%M:00')

            # For checking duration of the event, as it should not be more than 5 hours.

            # For checking event booking date and timings such that no past booking can be done such that for today's
            # date and the start_time as well as end_time should be greater than current time whereas the isoformat is
            # used for converting the time to the string and comparing the value with the form time values
            if (event_date == date_today and (event_start.isoformat() <= time_now)):
                raise forms.ValidationError("Please fill future timings")

            # Comparing the form_data with the values in database for checking already booked hall
            event_time = Booking.objects.filter(Q(start_time__range=(e_start)) | \
                                                Q(start_time__lte=event_start) | \
                                                Q(start_time__gte=event_start),
                                                date=event_date, doctor=doc)

            # If any any booking exists within the entered timgings then the Validation error occurs.
            for t in event_time:
                if t is not None:
                    raise forms.ValidationError("Doctor Already Booked")

            return form_data

        except KeyError:
            print("Please fill the entries")
            # If the exception is raised for KeyError, then the statement will execute till the required entries are filled


"""
This form is used for viewing the future booking in various hall and the user can filter the bookings by selecting the
date and/or the hall such that the list of bookings will be shown.
"""


class ViewBookingsForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['doctor', 'date']

