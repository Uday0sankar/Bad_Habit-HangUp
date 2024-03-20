from django.contrib import admin
from .models import Habits,Councilor,Booking

# Register your models here.
admin.site.register(Habits)
admin.site.register(Councilor)

class BookingAdmin(admin.ModelAdmin):
    list_display =('id','p_name','p_ph','coun_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)