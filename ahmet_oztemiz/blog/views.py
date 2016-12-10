from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from .forms import BlogEntryForm

# Create your views here.
from .models import BlogEntry

def create_blogs(request):
    if request.method == 'POST':
        formset = BlogEntryForm(request.POST)
        formset.save()
        return HttpResponse("Success!")
    else:
        formset = BlogEntryForm()
    return render(request, 'create_page.html', {'formset': formset})

def show_blogs(request):
    data = BlogEntry.objects.all()
    return render(request, "my_blogs.html", {"data": data, "user": request.user})

def get_blog(request, blog_id):
    one_entry = BlogEntry.objects.get(pk=int(blog_id)+1)
    title = one_entry.title
    body = one_entry.body
    try:
        return HttpResponse("<h1>"+title+"</h1><p>"+body+"</p>")
    except IndexError:
        raise Http404("We don't have any.")