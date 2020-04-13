from django.contrib import admin
from .models import Post, PostComment

# Registered Models for Admin dashboard
admin.site.register(Post)
admin.site.register(PostComment)
