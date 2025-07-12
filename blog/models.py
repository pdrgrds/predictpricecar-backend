from django.db import models
from django.conf import settings

class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría de Blog"
        verbose_name_plural = "Categorías de Blog"

    def __str__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="blog_covers/", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('BlogCategory', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('BlogTag', blank=True)
    prediction = models.ForeignKey(
        'predictions.PrediccionVehiculo',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
