from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.forms import RegistrationForm
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('capturing.views',
    url(r'^$', 'index', name='main'),
    url(r'^display-links/$', 'display_links', name='links'),
    url(r'^search/$', 'search', name='search'),
    # Examples:
    # url(r'^$', 'picker.views.home', name='home'),
    # url(r'^picker/', include('picker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    url(r'^accounts/register/$', 'registration.views.register', 
        {'backend': 'registration.backends.default.DefaultBackend',
         'form_class':RegistrationForm,
         'success_url':'/'}, 
        name="registration"),
    )

urlpatterns += patterns('django.contrib.auth.views',

    url(r'^login/$', 'login', 
        {'template_name'       : 'login/login.html',},
        name="user_login"),

    url(r'^logout/$', 'logout', 
        {'template_name': 'login/logout.html',},
        name="user_logout"),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += staticfiles_urlpatterns()
