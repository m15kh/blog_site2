from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE , null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_post'
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail_post', args=[self.pk])
