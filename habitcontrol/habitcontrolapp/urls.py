from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('habit/',views.habit,name='habit'),
    path('remarks/',views.remarks,name='remarks'),
    path('alcohol/',views.alcohol,name='alcohol'),
    path('proc/',views.alcohol,name='proc'),
    path('booking/',views.Booking,name='booking'),
    path('councilor/',views.Councilors,name='councilor'),
    path('about/',views.about,name='about'),
]
