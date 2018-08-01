from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>/', views.detail, name='detail'),
    path('rgif', views.rgif, name='rgif'),
]