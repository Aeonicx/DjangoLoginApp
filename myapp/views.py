import re
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.session.get('user_active', False) == True:
        return redirect('dashboard')
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
    
def dashboard(request):
    if request.session.get('user_active', False) == True:
        user = Users.objects.get(id=request.session.get('user_id'))
        context= {'user': user}
        return render(request, 'dashboard.html', context)
    return redirect('/')
    
def registration(request):
    if request.method == 'POST':
        try:
            name= request.POST.get('name').title()
            email= request.POST.get('email').lower()
            password= request.POST.get('password')
            image='uploads/default.png'
            if len(request.FILES) > 0:
                image= request.FILES.get('image')
            if Users.objects.filter(email=email).exists() :
                messages.warning(request, 'The Email is Already in Used, Try with another one!')
                return redirect('/register')
            else:
                Users.objects.create(name=name, email=email, password=password, image=image)
                messages.success(request, 'Your Register is Successful, Login Now!')
                return redirect('login')
        except:
            return redirect('/register')
    return redirect('/')
    
def signin(request):
    if request.method == 'POST':
        try:
            email= request.POST.get('email').lower()
            password= request.POST.get('password')
            if Users.objects.filter(email=email, password=password).exists() :  
                request.session['user_id'] = Users.objects.get(email=email).id
                request.session['user_active'] = True
                return redirect('dashboard')
            else:
                messages.warning(request, 'Invalid Credentials, Please check your Email and Password again!')
                return redirect('login')
        except:
            return redirect('/register')
    return redirect('/')
    
def signout(request):
    if request.method == 'POST':
        request.session['user_active'] = False
        return redirect('/')
    return redirect('/')

