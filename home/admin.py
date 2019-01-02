from django.contrib import admin
from .models import BlogPosts,BlogUser
# Register your models here.

admin.site.register(BlogPosts)
admin.site.register(BlogUser)
