from django.db import models

from markdownx.models import MarkdownxField


class Articles(models.Model):
    title = models.CharField(max_length=200)

    body = MarkdownxField()

    date = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=100)

    description = models.CharField(max_length=400)

    is_published = models.BooleanField()

    slug = models.SlugField(primary_key=True, max_length=250, unique=True)


class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.article)
    # Create your models here.
