from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from complaints.models import Complaint
from .models import Profile
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

# Signup
def signup_page(request):
    if request.user.is_authenticated:
        return redirect("home")


    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, "accounts/signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, "accounts/signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, "accounts/signup.html")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Signup successful! Please login.")
        return redirect("login")

    return render(request, "accounts/signup.html")

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    total = Complaint.objects.filter(user=request.user).count()
    resolved = Complaint.objects.filter(user=request.user, status="resolved").count()

    points = profile.green_points

    # Badge Logic
    if points >= 100:
        badge = "Green Champion"
    elif points >= 50:
        badge = "Clean Citizen"
    else:
        badge = "Beginner"

    return render(request, "accounts/profile.html", {
        "profile": profile,
        "total": total,
        "resolved": resolved,
        "points": points,
        "badge": badge,
    })

# Login
def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")


    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


# Logout
def logout_view(request):
    logout(request)
    return redirect("intro")

