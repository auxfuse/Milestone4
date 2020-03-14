from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


categories = [
    ('', ''),
    ('crossfit', 'Crossfit'),
    ('olympic weightlifting', 'Olympic Weightlifting'),
    ('powerlifting', 'Powerlifting'),
    ('general', 'General'),
    ('physiotherapy', 'physiotherapy'),
    ('health', 'Health'),
    ('nutrition', 'Nutrition'),
    ('gymnastics', 'Gymnastics'),
    ('personal training', 'Personal Training')
]


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    categories = models.CharField(max_length=21, choices=categories)
    originator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
