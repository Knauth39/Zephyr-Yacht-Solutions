# zeppelin/views.py

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect 
from .forms import RequestRegistrationForm

def requestRegistrationView(request):
    if request.method == "GET":
        form = RequestRegistrationForm
    else:
        form = RequestRegistrationForm(request.POST) 
        if form.is_valid():
            subject = "Zeppelin Account request"
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["info@zephyrsolutions.us"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "client.html", {"form": form})

def successView(request):
    return HttpResponse("Success!  Thank you for your message.")