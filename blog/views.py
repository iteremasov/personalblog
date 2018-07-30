from django.shortcuts import render
import giphypop
from .forms import CommentForm

from .models import Articles

from django.http import HttpResponse

from django.template.response import TemplateResponse

giphy = giphypop.Giphy()


def index(request):
    articles = Articles.objects.all()
    return TemplateResponse(request, 'index.html', {'articles': articles})


def detail(request, article_id):
    art = Articles.objects.get(pk=article_id)
    comments = art.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article_id = article_id
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'body_articl.html',
                  {'art': art,
                   'comments': comments,
                   'comment_form': comment_form})


# Create your views here.
def rgif(request):
    rgif = giphy.screensaver('funny')
    return TemplateResponse(request, 'rgif.html', {'source': rgif.id})

