from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Article


def index_view(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'index.html', context=context)


def article_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article': article})


def articles_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, content=content, author=author)
        return redirect('article_detail', pk=article.id)
