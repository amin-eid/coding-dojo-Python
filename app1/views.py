from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    users=User.objects.all()
    for user in users:
        if user.email==request.POST['email']:
            errors['email']="This email already exists in our database!"

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(fname=fname, lname=lname,email=email,password=pw_hash)
        request.session['fname']=User.objects.last().fname
        return redirect('/home')

def home(request):
    
    return render(request,'home.html')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['fname'] = logged_user.fname
            messages.success(request,"login successful!")
            return redirect('/home')
        messages.error(request,"invalid credentials!")
        return redirect('/')
    messages.error(request,"invalid credentials!")
    return redirect("/")   
        
