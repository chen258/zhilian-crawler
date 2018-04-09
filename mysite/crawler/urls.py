from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gocrawl', views.crawl),
    path('getcrawler', views.getcrawl),
]