from django.contrib import admin

from .models import Articles, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Articles)

# Register your models here.
