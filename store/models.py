from django.db import models
from korok.models import Hallgato

class Eszkoz(models.Model):
    name = models.CharField(blank=False, max_length=20)
    owner = models.ForeignKey(Hallgato, on_delete = models.CASCADE)
    expiration_date = models.DateField()
    store_id = models.SlugField(max_length = 10)

    def __str__(self):
        return self.name
