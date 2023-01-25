from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    context={
        'books':Book.objects.all()
    }
    return render(request,'form.html',context)

def addbook(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    else:
        Book.objects.create(title=request.POST['title'])
    return redirect('/')

def viewbook(request,id):
    context={
        'book':Book.objects.get(id=int(id)),
        'allpublishers':Publisher.objects.all()

    }
    return render(request,'viewbook.html',context)

def pubtobook(request,id):
    book1=Book.objects.get(id=int(id))
    pub1=Publisher.objects.get(id=request.POST['pubtobook'])
    book1.publishers.add(pub1)
    return redirect('/books/' +str(id))
