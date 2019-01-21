from django.http import JsonResponse

from blog.actions.articles import get_articles, get_article
from  django.forms.models import model_to_dict


def get_articles_controller(request):
    try:
        articles = get_articles(int(request.GET['page']), int(request.GET['pagesize']))
    except:
        articles = get_articles()

    print(articles)

    return JsonResponse(list(articles.values('body', 'title', 'date', 'slug')), safe=False)


def get_article_controller(request, slug):
    art = get_article(slug=slug)
    res = dict()
    for key in art._meta.get_fields():
        res[key] = getattr(art, key)

    return JsonResponse(res)


# def get_article_controller(request, slug):
#     art = get_article(slug=slug)
#     art_dict = {'date': art.date, 'data': model_to_dict(art)}
    art_dict = model_to_dict(art)
    # return JsonResponse(art_dict)

# def get_article_controller(request, slug):
#     article = get_article(slug=slug)
#
#     return (JsonResponse(model_to_dict(article))