from django.shortcuts import render, HttpResponse,redirect
from .models import *
# Create your views here.
def method1(request):
    return HttpResponse('hello world from Django app 1')

def form(request):
    context={
        'teachers':Teacher.objects.all()
    }
    return render(request,'index.html',context)

def tadd(request):
    Teacher.objects.create(name=request.POST['tname'])
    return redirect("/form")


def sadd(request):
    teacher1=Teacher.objects.get(id=request.POST['teacher'])

    Student.objects.create(name=request.POST['sname'],teacher=teacher1)
    return redirect("/form")

