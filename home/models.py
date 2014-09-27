from django.db import models
from django import forms


class Opinion(models.Model):
    opinion_key = models.CharField(max_length=25)
    opinion_value = models.CharField(max_length=255)

    def __str__(self):
        return "opinion_key:" + self.opinion_key + " opinion_value:" + self.opinion_value

    @staticmethod
    def get_opinion(key):
        if key is None:
            return False
        opinion_bean = Opinion.objects.filter(opinion_key=key)
        if opinion_bean.count() == 0:
            return False
        else:
            return Opinion.objects.get(opinion_key=key)

    @staticmethod
    def save_opinion(key, value):
        if key is None or value is None:
            return False
        opinion = Opinion.objects.get_or_create(opinion_key=key, defaults={'opinion_key': key, 'opinion_value': value})
        return opinion

    @staticmethod
    def del_opinion(key):
        if key is None:
            return False
        opinion_bean = Opinion.objects.filter(opinion_key=key)
        if opinion_bean.count() == 0:
            return False
        else:
            return opinion_bean.delete()