from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from tags.models import Tag



class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)


