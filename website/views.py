from django.shortcuts import render, redirect
#the below import is the django authetication system
from django.contrib.auth import authenticate, login, logout
#The below import allows to show messages on screen announcing login and logout
from django.contrib import messages

# Create your views here.
def home(request):
    #check to see if loggin in - the logic here works if they are posting
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, 'Invalid username or password, please try again')
            return redirect('home')
    #if ther are nost posting, just show the home page
    else:
        return render(request, 'home.html', {})

#def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})

