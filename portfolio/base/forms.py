from django import forms
from .models import *


class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials()
        fields = ['name', 'dept', 'description', 'image']