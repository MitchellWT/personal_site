from django.db import models
from django.db.models import CharField, URLField, IntegerField


class Subject(models.Model):
    class SubjectType(models.IntegerChoices):
        Undefined = 0, 'Undefined'
        Person = 1, 'Person'
        Landscape = 2, 'Landscape'
        Architecture = 3, 'Architecture'
    name = CharField(max_length=169, blank=True)
    display_name = CharField(max_length=69, blank=True)
    social_link = URLField(blank=True)
    subject_type = IntegerField(default=SubjectType.Undefined, choices=SubjectType.choices)

    def __str__(self):
        return self.name
