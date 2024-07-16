from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('ver_carro')
        else:
            return redirect('login')
    else:
        return render(request, 'usuarios/login.html')

def logout_user(request):
    logout(request)
   
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
           user = authenticate(request,username=username, password=password)
           login(request,user)
           return redirect('home')
    else:
        form = RegisterUserForm()
      
    context = {'form':form}
    return render(request,'usuarios/register_user.html',context)