from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BlogCategory, BlogTag
from .serializers import BlogCategorySerializer, BlogTagSerializer


class BlogCategoryListAPIView(APIView):
    """
    GET: Listar categorías de blog
    """
    def get(self, request):
        categories = BlogCategory.objects.all()
        serializer = BlogCategorySerializer(categories, many=True)
        return Response(serializer.data)


class BlogTagListAPIView(APIView):
    """
    GET: Listar tags de blog
    """
    def get(self, request):
        tags = BlogTag.objects.all()
        serializer = BlogTagSerializer(tags, many=True)
        return Response(serializer.data)
