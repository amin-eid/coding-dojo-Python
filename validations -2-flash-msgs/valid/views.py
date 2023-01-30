from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == "GET":
        form=RegisterForm()
        context={
            'form':form,
        }
        return render(request,"index.html",context)
    if request.method == "POST":
    # Bind the POST data to an instance of our RegisterForm
        bound_form = RegisterForm(request.POST)
    # Now test that bound_form using built-in methods!
    # *************************
        print(bound_form.is_valid()) # True or False, based on the validations that were set!
        if bound_form.is_valid():
            return render(request,"success.html")
        else:
            print(bound_form.errors) # Any errors in this form as a dictionary
            messages.error(request, bound_form.errors)
            return redirect("/")