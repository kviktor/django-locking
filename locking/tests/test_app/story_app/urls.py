# coding=utf-8
from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^ajax/admin/', include('locking.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('story_app.urls')),
    url(r'', include('staticfiles.urls')),
]
