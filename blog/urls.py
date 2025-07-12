from django.urls import path
from .views import (
    BlogCategoryListAPIView,
    BlogTagListAPIView,
    CreateBlogAPIView,
    UpdateBlogAPIView,
    DeleteBlogAPIView,
    RetrieveBlogAPIView,
    BlogPostDetailAPIView,
    BlogPostFilteredListAPIView,
)

urlpatterns = [
    path("categories/", BlogCategoryListAPIView.as_view(), name="blog-categories"),
    path("tags/", BlogTagListAPIView.as_view(), name="blog-tags"),
    path("create/", CreateBlogAPIView.as_view(), name="blog-create"),
    path("update/<int:pk>/", UpdateBlogAPIView.as_view(), name="blog-update"),
    path("delete/<int:pk>/", DeleteBlogAPIView.as_view(), name="blog-delete"),
    path("get/<int:pk>/", RetrieveBlogAPIView.as_view(), name="get-blog"),
    path("detail/<int:pk>/", BlogPostDetailAPIView.as_view(), name="blog-detail"),
    path("list-filtered/", BlogPostFilteredListAPIView.as_view(), name="blog-list-filtered"),
]
