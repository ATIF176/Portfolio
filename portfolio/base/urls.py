from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('reviews/', views.reviews, name='reviews'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
]
