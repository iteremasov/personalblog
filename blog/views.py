from django.shortcuts import render
import giphypop

from .models import Articles

from django.http import HttpResponse
from django.template.response import TemplateResponse

giphy = giphypop.Giphy()


def index(request):
    articles = Articles.objects.all()
    return TemplateResponse(request, 'index.html', {'articles': articles})


def detail(request, article_id):
    art = Articles.objects.get(pk=article_id)
    articles = Articles.objects.all()
    return TemplateResponse(request, 'body_articl.html', {'art': art})


def results(request, article_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % article_id)


def vote(request, article_id):
    return HttpResponse("You're voting on question %s." % article_id)


# Create your views here.
def rgif(request):
    rgif = giphy.screensaver('funny')
    return TemplateResponse(request, 'rgif.html', {'source': rgif.id})
