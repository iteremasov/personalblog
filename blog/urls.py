from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rgif', views.rgif, name='rgif')
]