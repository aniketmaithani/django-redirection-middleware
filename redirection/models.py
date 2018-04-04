from django.db import models
from simple_history.models import HistoricalRecords



class Redirection(models.Model):
    original_url = models.CharField(max_length=255)
    redirection_to = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Redirection'
        verbose_name_plural = 'Redirections'

    def __str__(self):
        return "{} -> {}".format(self.original_url, self.redirection_to)
