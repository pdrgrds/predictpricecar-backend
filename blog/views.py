from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BlogCategory, BlogTag, BlogPost
from .serializers import BlogCategorySerializer, BlogTagSerializer, BlogPostSerializer, BlogPostDetailSerializer, BlogPostFullSerializer
from rest_framework import viewsets, permissions, status, generics
from django.shortcuts import get_object_or_404

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

class CreateBlogAPIView(APIView):
    """
    API para crear un nuevo blog post
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateBlogAPIView(APIView):
    """
    API para editar un blog post existente
    """
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            blog = BlogPost.objects.get(pk=pk, author=request.user)
        except BlogPost.DoesNotExist:
            return Response(
                {"error": "Blog no encontrado o no tiene permisos."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BlogPostSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateBlogAPIView(APIView):
    """
    API para editar un blog post existente
    """
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            blog = BlogPost.objects.get(pk=pk, author=request.user)
        except BlogPost.DoesNotExist:
            return Response(
                {"error": "Blog no encontrado o no tiene permisos."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BlogPostSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteBlogAPIView(APIView):
    """
    API para eliminar (despublicar) un blog post
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            blog = BlogPost.objects.get(pk=pk, author=request.user)
        except BlogPost.DoesNotExist:
            return Response(
                {"error": "Blog no encontrado o no tiene permisos."},
                status=status.HTTP_404_NOT_FOUND
            )

        blog.published = False
        blog.save()
        return Response({"message": "Blog despublicado correctamente."})

class RetrieveBlogAPIView(APIView):
    """
    API para obtener un blog post por su ID
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        try:
            blog = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"error": "El blog no existe."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogPostSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogPostDetailAPIView(APIView):
    """
    API para obtener un blog con todas sus referencias
    """
    def get(self, request, pk):
        blog = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostDetailSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogPostFilteredListAPIView(generics.ListAPIView):
    """
    Listar blogs filtrados por categoría y/o etiquetas
    """
    serializer_class = BlogPostFullSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = BlogPost.objects.filter(published=True)
        category_id = self.request.query_params.get("category")
        tags_ids = self.request.query_params.getlist("tags")

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if tags_ids:
            queryset = queryset.filter(tags__id__in=tags_ids).distinct()
        return queryset
