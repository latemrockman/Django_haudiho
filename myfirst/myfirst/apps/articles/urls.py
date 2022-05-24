from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.article_page, name='article-page'),
    path('test/', views.test, name='test')
]