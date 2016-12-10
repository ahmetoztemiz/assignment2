from django.conf.urls import url
from .views import create_blogs, show_blogs, get_blog


urlpatterns = [
    url(r'^$', show_blogs, name="show_blogs"),
    url(r'^create/$', create_blogs, name="create_blogs"),
    url(r'^(?P<blog_id>[0-9]+)', get_blog)

]
