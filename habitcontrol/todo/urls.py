from django.urls import path
from . import views

urlpatterns = [
    path("todo/",views.todofn,name='todo'),
     path('delete/<int:del_id>/',views.delete,name='delete'),
]