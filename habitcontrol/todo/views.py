from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo

# Create your views here.
def todofn(request):
    item=todo.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        obj=todo(name=name,desc=desc)
        obj.save()
    return render(request,'todolist.html',{'items':item})
def delete(request,del_id):
    item=todo.objects.get(id=del_id)
    item.delete()
    return redirect('/')