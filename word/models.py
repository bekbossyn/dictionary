from django.contrib.postgres.fields import JSONField
from django.db import models

from utilities.time_utilities import dt_to_timestamp


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=200, blank=True, null=True)
    data = JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"Id = {0} Word = {1}".format(self.pk, self.word)
    
    def json(self):
        return {
            "id": self.pk,
            "word": self.word,
            "data": self.data,
            "timestamp": dt_to_timestamp(self.timestamp),
        }

    class Meta:
        ordering = ['timestamp']


class Language(models.Model):
    code_name = models.CharField(max_length=20, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    # data = JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"Id = {0} Language display name = {1}".format(self.pk, self.display_name)

    def json(self):
        return {
            "id": self.pk,
            "code_name": self.code_name,
            "display": self.display_name,
            "timestamp": dt_to_timestamp(self.timestamp),
        }

    class Meta:
        ordering = ['timestamp']

