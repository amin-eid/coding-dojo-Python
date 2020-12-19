from django.shortcuts import render,redirect
from .models import dojo,ninja
def index(request):
    context = {
        "allDojos": dojo.objects.all()
    }
    return render(request, "index.html", context)
    
def addDojo(request):
    dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
    return redirect('/')
    
def addNinja(request):
    x=request.POST['dojo']
    y=dojo.objects.get(name=x)
    print("*" *30)
    print(dojo.objects.get(name=x))
    print(y.id)
    print("*" * 30)
    ninja.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],dojo=dojo.objects.get(name=x))
    return redirect('/')