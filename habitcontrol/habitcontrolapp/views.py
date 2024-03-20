from django.shortcuts import render
from .models import Habits,Councilor
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def habit(request):
    dict_hab={
        'hab':Habits.objects.all()
        }
    return render(request,'habit.html',dict_hab)
def remarks(request):
    return render(request,'remark.html')
def alcohol(request):
    return render(request,'alcohol.html')
def proc(request):
    return render(request,'proc.html')

# councilor booking

def Booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

# councilor
def Councilors(request):
    dict_coun={
        'coun':Councilor.objects.all()
        }
    return render(request,'councilor.html',dict_coun) 
def about(request):
    return render(request,'about.html')