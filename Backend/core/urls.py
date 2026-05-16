from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro, name="intro"),
    path("home/", views.home, name="home"),   
    path("hub/", views.hub, name="hub"),
    path('contact/', views.contact_view, name='contact'),

]
