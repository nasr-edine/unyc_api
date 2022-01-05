from django.db import models


class Reference(models.Model):
    ref = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.ref
