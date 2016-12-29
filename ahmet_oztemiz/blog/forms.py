from .models import BlogEntry
from django import forms


class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ("title", "body", "tags")