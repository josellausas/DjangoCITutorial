"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.tasks import views as task_views
from apps.tasks import urls as task_urls
from apps.leads import urls as lead_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Index
    url(r'^$', task_views.index, name="index"),
    # Tasks
    url(r'^tasks/', include(task_urls)),
    # Leads
    url(r'^leads/', include(lead_urls)),
]
