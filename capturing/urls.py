from django.conf.urls import patterns, include, url

urlpatterns = patterns('capturing.views',
	url(r'^$', 'main_page', name='main'),
    url(r'^capture/$', 'capture', name='capture'),
 	url(r'^display-links/$', 'display_links', name='links'),
    url(r'^search/$', 'search', name='search'),
)