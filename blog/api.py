from django.http import JsonResponse

from blog.actions.articles import get_articles


def get_articles_controller(request):
    try:
        articles = get_articles(int(request.GET['page']), int(request.GET['pagesize']))
    except:
        articles = get_articles()

    print(articles)

    return JsonResponse(list(articles.values('body', 'title', 'date')), safe=False)
