from django.conf.urls import url
from .views import show_blogs, get_blog, show_all_user_blogs, show_selected_user_blogs


urlpatterns = [
    url(r'^$', show_blogs, name="show_blogs"),
    url(r'^(?P<blog_id>[0-9]+)', get_blog, name="get_blog"),
    url(r'^entries/$', show_blogs, name="show_blogs"),
    url(r'^entries/(?P<blog_id>[0-9]+)', get_blog),
    url(r'^entries/all/$', show_all_user_blogs, name="show_all_users_blogs"),
    url(r'^entries/all/user/(?P<userId>[0-9]+)$', show_selected_user_blogs, name="show_selected_user_blogs")

]
