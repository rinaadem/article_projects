from django.urls import path
from webapp.views import index_view, articles_create_view, article_view

urlpatterns = [
    path('', index_view, name='articles'),
    path('create/', articles_create_view, name='article_add'),
    path('article/<int:pk>/', article_view, name='article_detail'),
]
