from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import BlogEntry
from .forms import BlogEntryForm


def show_blogs(request):

    if request.method == "POST":
        form = BlogEntryForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            form._save_m2m()
    elif request.method == "GET":
        form = BlogEntryForm()


    return render(request, "my_blogs.html", {"blogs": BlogEntry.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all(),
                                             "form": form})

def get_blog(request, blog_id):
    try:
        blog = BlogEntry.objects.get(id=blog_id)
        if request.user.id != blog.owner.id:
            raise PermissionDenied
        return render(request, "create_page.html", {"blog": blog})
    except BlogEntry.DoesNotExist:
        raise Http404("There is no result!")