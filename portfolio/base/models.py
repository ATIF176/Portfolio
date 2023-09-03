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
    

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    authname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
