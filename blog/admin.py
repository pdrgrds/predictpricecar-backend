from django.contrib import admin
from .models import BlogCategory, BlogTag, BlogPost

admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(BlogTag)
