from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # core pages
    path("", include("core.urls")),

    # accounts (login/signup)
    path("accounts/", include("accounts.urls")),

    # ✅ THIS LINE IS MANDATORY
    path("complaints/", include("complaints.urls")),
    path('', include('core.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)