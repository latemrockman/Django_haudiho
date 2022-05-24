from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Article, Comment

# Create your views here.

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'all_articles': latest_articles_list})


def article_page(request, article_id):
    try:
        article = Article.objects.get( id=article_id)
    except:
        raise Http404('Статья не найтена')

    return render(request, 'articles/article_page.html', {'article': article, 'article_id': article_id})


#article_titles
#article_text =
#pub_date = mod
#
#

def test(request):
    return HttpResponse('Test')



