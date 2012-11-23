from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.forms import RegistrationForm, RegistrationFormUniqueEmail
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    (r'', include('capturing.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('registration.views',
    url(r'^register/$', 'register', 
        {'backend': 'registration.backends.default.DefaultBackend',
         'form_class':RegistrationFormUniqueEmail,
         'success_url':'/'}, 
        name="registration"),
    url(r'^profile/$', 'profile', name = 'profile'),
    (r'^accounts/', include('registration.backends.default.urls')),
    )

urlpatterns += patterns('django.contrib.auth.views',

    url(r'^login/$', 'login', 
        {'template_name'       : 'login/login.html',
         'redirect_field_name' : 'next'},
        name="user_login"),

    url(r'^logout/$', 'logout', 
        {'template_name': 'login/logout.html',},
        name="user_logout"),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
