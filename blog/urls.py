from django.urls import path
from .views import (
    BlogCategoryListAPIView,
    BlogTagListAPIView
)

urlpatterns = [
    path("categories/", BlogCategoryListAPIView.as_view(), name="blog-categories"),
    path("tags/", BlogTagListAPIView.as_view(), name="blog-tags"),
]
