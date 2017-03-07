from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='task_index'),
    url(r'^new$', views.index, name='task_new'),
    url(r'^(\d+)/$', views.detail, name='task_detail'),
]
