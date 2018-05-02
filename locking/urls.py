# coding=utf-8
from django.conf.urls import url
try:
    from django.views.i18n import JavaScriptCatalog
except ImportError:  # django 1.9
    from django.views.i18n import javascript_catalog

from . import views

urlpatterns = [
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/lock/$',
        views.lock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/unlock/$',
        views.unlock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/is_locked/$',
        views.is_locked),
    url(r'variables\.js$', views.js_variables, name='locking_variables'),
]

try:
    urlpatterns += [
        url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['locking']),
            name='javascript-catalog'),
    ]
except NameError:  # django 1.9
    urlpatterns += [
        url(r'^jsi18n/$', javascript_catalog, kwargs={'package': 'locking'},
            name='javascript-catalog'),
    ]
