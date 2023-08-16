from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('handlelogin/', views.handlelogin, name='handlelogin'),
    path('handlelogout/', views.handlelogout, name='handlelogout'),
]