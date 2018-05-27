from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<post_id>\d+)/$',views.detail,name = 'detail'),
]
