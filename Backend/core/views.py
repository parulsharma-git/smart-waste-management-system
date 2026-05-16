
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def intro(request):
    return render(request, "core/intro.html")


@login_required
def home(request):
    return render(request, "core/index.html")  # Protected page after login

def hub(request):
    return render(request, "core/hub.html")

def contact_view(request):
    return render(request, "core/contact.html")