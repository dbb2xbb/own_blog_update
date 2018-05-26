from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/(\d+)/$',views.detail,name = 'detail'),
]
