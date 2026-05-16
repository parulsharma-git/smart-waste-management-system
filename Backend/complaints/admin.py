from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('location', 'user__username')