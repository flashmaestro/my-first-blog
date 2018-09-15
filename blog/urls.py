from django.conf.urls import url
from . import views
urlpatterns = [
    #/
    #/test/
    url(r'^$', views.post_list, name='post_list'),
    # naver.com/post/1
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]