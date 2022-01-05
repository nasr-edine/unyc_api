from django.db import models


class Reference(models.Model):
    ref = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.ref

    # def get_absolute_url(self):
    #     return reverse("References_detail", kwargs={"pk": self.pk})
