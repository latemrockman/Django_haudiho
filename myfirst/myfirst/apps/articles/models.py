from django.db import models

# Create your models here.


class Article(models.Model):
    article_titles = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_titles

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.autor_name