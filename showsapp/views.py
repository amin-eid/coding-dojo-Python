from django.shortcuts import render, HttpResponse,redirect
from .models import shows
from django.utils.dateparse import parse_date
from datetime import datetime,date
def index(request):
    return redirect('/shows')


def show(request):
    context = {
        "allshows": shows.objects.all()
    }
    return render(request, "index.html", context)


def addshow(request):
    return render(request, "addshow.html")


def showsadd(request):
    title=request.POST['title']
    print(title)
    network=request.POST['network']
    date=request.POST['date']
    #date=date1.strftime("%Y/%m/%d")
    #date = parse_date(date1)
    print("*"*30)
    print(date)
    print("*"*30)
    description=request.POST['description']
    shows.objects.create(title=title,network=network,release_date=date,description=description)
    last=shows.objects.last()
    id=last.id
    return redirect(f"/shows/{id}")


def show_id(request,id):
    show1=shows.objects.get(id=id)
    context={
        'show':show1,
    }
    return render(request,"show_id.html",context)

def delete(request,id):
    show_to_delete=shows.objects.get(id=id)
    show_to_delete.delete()
    return redirect('/')

def edit(request,id):
    show_to_edit=shows.objects.get(id=id)
    context={
        'show':show_to_edit,
    }
    return render(request,"editshow.html",context)

def edit2(request,id):
    show_to_edit=shows.objects.get(id=id)
    title=request.POST['title']
    network=request.POST['network']
    date=request.POST['date']
    description=request.POST['description']
    show_to_edit.title=title
    show_to_edit.network=network
    show_to_edit.release_date=date
    show_to_edit.description=description
    print("***********************************10101010************************")
    show_to_edit.save()
    return redirect("/")