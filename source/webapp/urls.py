from django.urls import path
from webapp.views import index_view, articles_create_view, article_view

urlpatterns = [
    path('', index_view),
    path('create/', articles_create_view),
    path('article/<int:pk>/', article_view)
]
