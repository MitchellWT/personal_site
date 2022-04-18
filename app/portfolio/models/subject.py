from django.db import models
from django.db.models import CharField, URLField


class Subject(models.Model):
    name = CharField(max_length=169)
    display_name = CharField(max_length=69)
    social_link = URLField()

    def __str__(self):
        return self.name
