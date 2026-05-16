from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='home'),  
    path("signup/", views.signup_page, name="signup"),
    path("login/", views.login_page, name="login"),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
    
]



