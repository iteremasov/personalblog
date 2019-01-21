from django.contrib import admin

from .models import Articles, Comment

from markdownx.admin import MarkdownxModelAdmin


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Comment, CommentAdmin)
admin.site.register(Articles, MarkdownxModelAdmin)

# Register your models here.
