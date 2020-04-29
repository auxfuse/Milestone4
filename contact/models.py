from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Models
class Contact(models.Model):
    """Model to define the fields required to create Contact Form"""
    query_title = models.CharField(max_length=150)
    query_text = models.TextField()
    query_email = models.EmailField()
    date_posted = models.DateTimeField(default=timezone.now)
    query_from = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.query_title}, {self.query_email}'
