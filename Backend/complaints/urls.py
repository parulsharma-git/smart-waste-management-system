from django.urls import path
from . import views

app_name = "complaints"   # 👈 THIS LINE IS NON-NEGOTIABLE

urlpatterns = [
    path("new/", views.new_complaint, name="new"),
    path("my/", views.my_complaints, name="my_complaints"),
]

