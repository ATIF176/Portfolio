from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name + ' - ' + self.email
    

class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Projects(models.Model):
    projectname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    img1 = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    img2 = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    img3 = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    ltitle = models.CharField(max_length=100)
    etitle = models.CharField(max_length=100)
    cate = models.CharField(max_length=100)
    filterby = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    desc = models.TextField()
    comdate = models.DateField()
    llink = models.URLField(max_length=200)
    glink = models.URLField(max_length=200)

    def __str__(self):
        return self.projectname +" - "+ self.cate
    

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    authname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
