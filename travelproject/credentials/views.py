from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('credentials/login')
    return render(request,'login.html')
# Create your views here.
def registration(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password1']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Exists already')
                return redirect('registration')
            else:

                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            print('password not matched')
            messages.info(request, "Password not matching")
            return redirect('registration')

        return  redirect('/')
    return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')