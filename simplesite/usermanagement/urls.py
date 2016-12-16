from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^add$', views.post_new, name='post_new'),
    url(r'^list$', views.list_all, name='list_all'),
]