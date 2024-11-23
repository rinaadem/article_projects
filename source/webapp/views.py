from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.article_db import ArticleDB


# Create your views here.

def index_view(request):
    context = {
        'name': 'User 1',
        'age': 20,
        'articles': ArticleDB().articles,
        'my_img': 'img/2.png'
    }
    return render(request, 'index.html', context=context)

def articles_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        article = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author'),
        }
        ArticleDB.articles.append(article)
        return HttpResponseRedirect('/')
        # return render(request, 'article.html', context={'article': article})