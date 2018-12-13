from blog.models import Articles


def get_articles(page=1, pagesize=10):
    return Articles.objects.all().order_by('date')[:page * pagesize]


def get_article(slug):
    return Articles.objects.get(pk=slug)
