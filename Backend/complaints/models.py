from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    garbage_type = models.CharField(
        max_length=100,
        default="General"
    )

    severity = models.CharField(
        max_length=50,
        default="Low"
    )

    location = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(
        upload_to="complaints/",
        blank=True,
        null=True
    )

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.location}"