import datetime
from django.db import models
from django.utils import timezone


class Headline(models.Model):
    headline_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.headline_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Article(models.Model):
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)
    article_text = models.CharField(max_length=200)
    def __str__(self):
        return self.article_text