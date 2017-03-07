from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new$', views.index, name='lead_new'),
    url(r'^(\d+)/$', views.index, name='lead_list'),
]
