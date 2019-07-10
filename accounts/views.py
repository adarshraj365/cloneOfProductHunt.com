from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1 == password2):
            try:
                user = User.objects.get(username=username)
                return render(request,'accounts/acc.html',{'error':'User already exist ' } )
            except :
                user = User.objects.create_user(username=username,email=None,password=password1)
                auth.login(request,user)
                return redirect('home')
            
        else :

            return render(request,'accounts/acc.html',{'error':'Password not match Please try again' } )

    else :
        return render(request,'accounts/acc.html' )
def login(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            return render(request,'accounts/login.html',{'error':'please enter valid password'})

    else:
        return render(request,'accounts/login.html')
def logout(request):
    if request.method =='POST':
        auth.logout(request)
        return redirect('home')

