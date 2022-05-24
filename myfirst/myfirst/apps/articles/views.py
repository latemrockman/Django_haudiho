from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse

# Create your views here.

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html', {'all_articles': latest_articles_list})


def article_page(request, article_id):


    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    #comments = Comment.objects.filter(article=article)
    comments = article.comment_set.order_by('-id')[:10]

    return render(request, 'articles/article_page.html', {'article': article, 'comments': comments})



def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    article.comment_set.create(autor_name= request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(article.id,)))

#article_titles
#article_text =
#pub_date = mod
#
#

def test(request):
    return HttpResponse('Test')



