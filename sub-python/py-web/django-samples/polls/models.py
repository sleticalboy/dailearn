import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=256, verbose_name='投票主题')
    pub_date = models.DateTimeField(verbose_name="发布日期")

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='是否最近发布',
    )
    def was_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    pass


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256, verbose_name='投票选项')
    votes = models.IntegerField(default=0, verbose_name='票数')
    pass
