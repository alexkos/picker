from django.conf.urls import patterns, include, url

urlpatterns = patterns('capturing.views',
    url(r'^$', 'index', name='main'),
 	url(r'^display-links/$', 'display_links', name='links'),
    url(r'^search/$', 'search', name='search'),
)