from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.article_page, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave-comment'),
    path('test/', views.test, name='test')
]