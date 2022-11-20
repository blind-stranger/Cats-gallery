from django.db import models


class Photo(models.Model):
    image = models.ImageField()
    priority = models.PositiveSmallIntegerField(default=0)
    thumbnail = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.image.name
