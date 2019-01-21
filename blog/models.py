from django.db import models
# from ckeditor.fields import RichTextField

from markdownx.models import MarkdownxField


class Articles(models.Model):
    title = MarkdownxField()

    body = MarkdownxField()

    date = models.DateTimeField(auto_now_add=True)

    category = MarkdownxField()

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
