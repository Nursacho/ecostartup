from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User


from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})


class PostImage(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='blog_images')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title}.jpg'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 680:
            output_size = (400, 680)
            img.thumbnail(output_size)
            img.save(self.image.path)
