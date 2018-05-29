from django.shortcuts import render

from .models import Articles

from django.http import HttpResponse


def index(request):
    latest_question_list = Articles.objects.order_by('-date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse('Hello world' + output)


def detail(request, article_id):
    return HttpResponse("You're looking at Article %s." % article_id)


def results(request, article_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % article_id)


def vote(request, article_id):
    return HttpResponse("You're voting on question %s." % article_id)

# Create your views here.
