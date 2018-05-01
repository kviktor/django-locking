from django.conf.urls import url
from django.views.i18n import JavaScriptCatalog

from . import views

urlpatterns = [
    # verwijst naar een ajax-view voor het lockingmechanisme
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/lock/$', views.lock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/unlock/$', views.unlock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/is_locked/$',
     views.is_locked),
    url(r'variables\.js$', views.js_variables, name='locking_variables'),
]

urlpatterns += [
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['locking']),
        name='javascript-catalog'),
]
