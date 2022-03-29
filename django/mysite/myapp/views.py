from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from .models import EMPLOYEE
from .models import STORES
# Create your views here.
def index(request):
    employee_list = EMPLOYEE.objects.all()
    context = {
        "employee_list" : employee_list
    }

    stores_list = STORES.objects.all()
    context1 = {
        "stores_list" : stores_list
    } 
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, "myapp/index.html",context)
    return render(request, "myapp/index.html",context1)
    


@csrf_protect
def home(request):
    return render(request, "myapp/index.html")
#def signin(request):
    #return render(request,"myapp/signin.html")
def signup(request):
    #return render(request, "myapp/signup.html")
    #messages.success(request,"Your account has been successfully created")

    #return redirect("signin")
    if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        email =  request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        myuser = User.objects.create_user(username, email, pass1)
        #myuser = User.objects.create(username,email,pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect("signin")
    return render(request, "myapp/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"myapp/index.html",{"fname": fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect("home")

    return render(request,"myapp/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("myapp/index.html")

def admin(request):
    return render(request, "myapp/admin.py")