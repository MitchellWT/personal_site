from django.db import models
from django.db.models import ImageField, CharField, ManyToManyField, SlugField
from django.utils.text import slugify
from markdownx.models import MarkdownxField


class Project(models.Model):
    cover_image = ImageField(upload_to='cover_image')
    title = CharField(max_length=69)
    slug = SlugField(max_length=69)
    technology_used = ManyToManyField('TechnologyUsed')
    body = MarkdownxField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
