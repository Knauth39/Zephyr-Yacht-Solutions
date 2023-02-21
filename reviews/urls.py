# reviews/urls.py

from django.urls import path 
from .views import ReviewListView, UserWriteReview

urlpatterns = [
    path("", ReviewListView.as_view(), name="home"),
    path("reviews/", UserWriteReview, name="reviews")
]

