from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.forms import ModelForm


class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()



