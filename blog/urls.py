from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('CV', views.CV, name='CV'),

    # API Methods for react app

    path('api/articles', api.get_articles_controller),
    path('api/articles/<slug>/', api.get_article_controller)
]
