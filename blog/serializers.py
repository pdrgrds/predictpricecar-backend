from rest_framework import serializers
from .models import BlogCategory, BlogTag, BlogPost
from predictions.serializers import PrediccionVehiculoSerializer
from predictions.models import PrediccionVehiculo
from auth_app.serializers import CustomUserSerializer

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = "__all__"

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
        read_only_fields = [
            "id",
            "author",
            "created_at",
            "updated_at",
            "views_count",
            "published_at",
        ]

class BlogPostDetailSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()
    tags = BlogTagSerializer(many=True)
    author = CustomUserSerializer()
    prediction = PrediccionVehiculoSerializer()

    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogPostFullSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()
    tags = BlogTagSerializer(many=True)
    author = CustomUserSerializer()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "category",
            "tags",
            "title",
            "slug",
            "excerpt",
            "content",
            "created_at",
            "author",
            "cover_image"
        ]