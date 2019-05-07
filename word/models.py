from django.db import models
from utilities.time_utilities import dt_to_timestamp


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"Id = {0} Word = {1}".format(self.pk, self.word)
    
    def json(self):
        return {
            "id": self.pk,
            "word": self.word,
            "timestamp": dt_to_timestamp(self.timestamp),
        }

    class Meta:
        ordering = ['timestamp']

