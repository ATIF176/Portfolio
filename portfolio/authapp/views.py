from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        print(get_email, get_password, get_confirm_password)
        if get_password != get_confirm_password:
            messages.error(request, 'Password and Confirm Password does not match')
            return redirect('signup')
        try:
            if User.objects.get(email=get_email):
                messages.error(request, 'Email already exists')
                return redirect('signup')
        except:
            pass
        user = User.objects.create_user(username=get_email, email=get_email, password=get_password)
        user.save()
        messages.success(request, 'User created successfully')
        return redirect('handlelogin')

    return render(request, 'signup.html')

def handlelogin(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        myuser = authenticate(username=get_email, password=get_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'User logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('handlelogin')
    return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, 'User logged out successfully')
    return render(request, 'login.html')