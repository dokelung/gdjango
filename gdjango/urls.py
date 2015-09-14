from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^manage/', 'gdjango.views.manage'),
    url(r'^project_settings', 'gdjango.views.project_settings'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'gdjango.views.testform'),
)
