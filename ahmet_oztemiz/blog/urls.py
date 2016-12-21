from django.conf.urls import url
from .views import show_blogs, get_blog


urlpatterns = [
    url(r'^$', show_blogs, name="show_blogs"),
    url(r'^(?P<blog_id>[0-9]+)', get_blog),
    url(r'^entries/$', show_blogs, name="show_blogs"),
    url(r'^entries/(?P<blog_id>[0-9]+)', get_blog)

]
