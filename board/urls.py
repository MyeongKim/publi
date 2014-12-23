from django.conf.urls import patterns, include, url
from . import views, feed

urlpatterns = patterns(
    '',
    url(r'^$', views.Timeline.as_view(), name="index"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^ss', views.createPost , name = "plz"),
    url(r'^(?P<slug>\S+)$', views.Post.as_view(), name="entry_detail"),


    )