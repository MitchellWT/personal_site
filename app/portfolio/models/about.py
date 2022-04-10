from django.db import models
from markdownx.models import MarkdownxField


class About(models.Model):
    body = MarkdownxField()

    def __str__(self):
        return "About"
