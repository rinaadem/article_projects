from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.models import Article


def index_view(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'index.html', context=context)

def article_view(request):
    article_id = request.GET.get('id')
    article = Article.objects.get(id=article_id)
    return render(request, 'article_view.html', {'article': article})

def articles_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        Article.objects.create(title=title, content=content, author=author)
        return HttpResponseRedirect('/')
