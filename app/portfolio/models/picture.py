from django.db import models
from django.db.models import ImageField, CharField, DateField, ManyToManyField
from django.utils.text import slugify


class Picture(models.Model):
    picture_image = ImageField(upload_to='picture_image')
    title = CharField(max_length=69)
    slug = CharField(max_length=69)
    location = CharField(max_length=169)
    taken_date = DateField()
    subjects = ManyToManyField('Subject', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Picture, self).save(*args, **kwargs)
