# reviews/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Review
from .forms import WriteReview

class ReviewListView(ListView):
    model = Review 
    template_name = "home.html"

class UserWriteReview(WriteReview):
    template_name = "write_review.html"

def contactView(request):
    if request.method == "GET":
        form = WriteReview
    else:
        form = WriteReview(request.POST) 
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contact.html", {"form": form})

def successView(request):
    return HttpResponse("Success!  Thank you for your message.")