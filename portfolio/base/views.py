from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html',)

def about(request):
    return render(request, 'about.html',)

def contact(request):
    if request.method == "POST":
        name = request.POST('name')
        email = request.POST('email')
        phone = request.POST('num')
        message = request.POST('message')
        print(name, email, phone, message)
        messages.info(request, f'{name} your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html',)

def resume(request):
    return render(request, 'resume.html',)

def services(request):
    return render(request, 'services.html',)

