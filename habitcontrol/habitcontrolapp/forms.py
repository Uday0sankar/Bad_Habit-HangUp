from django import forms
from .models import Booking
class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        
        widgets={
            'booking_date':DateInput(),
        }
        labels ={
            'p_name':"Your Name :",
            'p_ph':"Your Phone :",
            'coun_name':"Name of Councilor:",
            'booking_date': "Booking Date :",
           
        }