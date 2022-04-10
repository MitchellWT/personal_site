from django.db import models
from django.db.models import CharField, ImageField


class TechnologyUsed(models.Model):
    name = CharField(max_length=256)
    image = ImageField(upload_to='technology_used')

    def __str__(self):
        return self.name
