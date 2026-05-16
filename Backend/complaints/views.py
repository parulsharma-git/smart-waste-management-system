from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Complaint

@login_required
def new_complaint(request):
    if request.method == "POST":
        Complaint.objects.create(
            user=request.user,
            garbage_type=request.POST.get("garbage_type"),
            severity=request.POST.get("severity"),
            location=request.POST["location"],
            description=request.POST["description"],
            image=request.FILES.get("image"),
        )

         # ✅ Add Green Points here
        request.user.profile.green_points += 10
        request.user.profile.save()
        return render(request, "complaints/success.html")

    return render(request, "complaints/new.html")




@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, "complaints/list.html", {"complaints": complaints})


def success(request):
    return render(request, "complaints/success.html")

