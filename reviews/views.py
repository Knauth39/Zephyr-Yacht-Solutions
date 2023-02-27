# reviews/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Review
from .forms import WriteReview

class ReviewListView(ListView):
    model = Review 
    template_name = "home.html"

