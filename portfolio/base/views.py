from email.mime import image
from tokenize import Pointfloat
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from base.models import Contact , Blog, Testimonials, Projects

# Create your views here.
def home(request):
    return render(request, 'home.html',)

def about(request):
    return render(request, 'about.html',)

def contact(request):
    if request.method == "POST":
        fname = request.POST['name']
        femail = request.POST['email']
        fphone = request.POST['num']
        fmessage = request.POST['desc']
        query = Contact(name=fname, email=femail, phonenumber=fphone, description=fmessage)
        query.save()
        messages.info(request, f'{fname} Thanks for contacting us! We will get back to you soon.')
        return redirect('/contact')
    
    return render(request, 'contact.html',)

def resume(request):
    return render(request, 'resume.html',)

def portfolio(request):
    projects = Projects.objects.all()
    context = {'projects':projects}
    return render(request, 'portfolio.html',context)

def portfolio_details(request, slug_url):
    project = Projects.objects.get(slug=slug_url)
    print(project)
    context = {'project':project}
    return render(request, 'portfolio-details.html', context)

def testimonials(request):
    if request.method == "POST":
        fname = request.POST['name']
        fposition = request.POST['position']
        fimg = request.FILES.get('img', None)
        print(fimg)
        fmessage = request.POST['desc']
        try:
            # Create and save the Testimonials instance
            query = Testimonials(name=fname, dept=fposition, image=fimg, description=fmessage)
            query.save()
            messages.info(request, f'Thank you, {fname}, for your feedback!')
        except Exception as e:
            # Handle exceptions, e.g., database errors
            messages.error(request, f'Error: {str(e)}')
        return redirect('/reviews')

    feedbacks = Testimonials.objects.all()[:5]
    context={'feedbacks':feedbacks}
    
    return render(request, 'testimonials.html', context)

def reviews(request):
    return render(request, 'review_form.html',)

def services(request):
    return render(request, 'services.html',)

def blog(request):
    posts = Blog.objects.all()
    context = {'posts':posts}
    return render(request, 'blog.html', context)

