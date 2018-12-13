from django.shortcuts import render
import giphypop

from blog.actions.articles import get_articles, get_article
from .forms import CommentForm

from django.template.response import TemplateResponse

giphy = giphypop.Giphy()


def index(request):
    return TemplateResponse(request, 'index.html', {'articles': get_articles()})


def detail(request, slug):
    art = get_article(slug)
    comments = art.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = art
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
    rgif = giphy.screensaver('cats')
    return TemplateResponse(request, 'rgif.html', {'source': rgif.id})


def CV(request):
    return TemplateResponse(request, 'CV.html', {})
