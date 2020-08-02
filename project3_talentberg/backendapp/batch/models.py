from django.db import models


class Batch(models.Model):
    batchtime = models.CharField(max_length=100)