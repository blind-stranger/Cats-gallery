from django.db import models

class Photo(models.Model):
    image = models.ImageField()
    priority = models.PositiveSmallIntegerField(default=0)