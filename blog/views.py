from django.shortcuts import render
import giphypop

from .models import Articles

from django.http import HttpResponse
from django.template.response import TemplateResponse

giphy = giphypop.Giphy()


def index(request):
    # articles = Articles.objects.order_by('-date')[:5]
    # output = ', '.join([a.title for a in articles])
    articles = Articles.objects.all()
    # return HttpResponse('Hello world ' + output)
    # return render(request, 'index.html', output)
    # return TemplateResponse(request, 'index.html', output)
    return TemplateResponse(request, 'index.html', {'articles': articles})


def detail(request, article_id):
    return HttpResponse("You're looking at Article %s." % article_id)


def results(request, article_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % article_id)


def vote(request, article_id):
    return HttpResponse("You're voting on question %s." % article_id)


# Create your views here.
def rgif(request):
    rgif = giphy.screensaver('funny')
    return TemplateResponse(request, 'rgif.html', {'source': rgif.id})
