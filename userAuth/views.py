from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import Technology
# Create your views here.

# def homePage(request):
#     if request.method == "POST":
        

def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginUser')
    else:
        form = SignUpForm()

    return render(request,'signup.html',{'form':form})

def loginUser(request):
    try:
        if request.user.is_authenticated:
            return redirect('homePage')
    except:
        print("Error")
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request,user)
                    expertise = Technology.objects.filter(userTech=request.user)
                    if not expertise:
                        return redirect('addTech')
                    else:
                        return redirect('homePage')
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    

def logoutUser(request):
    logout(request)
    return redirect('loginUser')

def addTech(request):
    techStack = request.POST.get('technology')
    userObj = Technology.objects.create(userTech=request.user,technology=techStack)
    
    return redirect('homePage')

def homePage(request):
    userObj = Technology.objects.filter(userTech=request.user).first()
    return render(request,'homePage.html',{'userObj':userObj})