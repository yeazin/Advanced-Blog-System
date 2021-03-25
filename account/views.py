from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogUser_Forms
from .models import New_User_Custom


#user = New_User_Custom()

# for user registration

def Create_User(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        forms = BlogUser_Forms() 
        if request.method == "POST":
            forms = BlogUser_Forms(request.POST)
            if forms.is_valid():
                forms.save()
                user = forms.cleaned_data.get('user_name')
                return redirect ('login')
        else:
            forms = BlogUser_Forms()


    context ={'forms':forms}
    return render (request,'account/createuser.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:

        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = authenticate(request, email = email, password = password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request,'Sorry! emali or Password ')

    context ={}
    return render (request,'account/login.html', context)

# User log-out
def user_logout(request):
    logout(request)
    return redirect('/')


#for user dashboard 
@login_required( login_url= 'login')   
def Dashboard(request):
    context ={}
    return render (request, 'account/dashboard.html', context)