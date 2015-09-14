from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home', 'alcom.views.home', name='home'),
    url(r'^news', 'news.views.list_news'),
    url(r'^people/advisor', 'lab.views.show_advisor'),
    url(r'^people/former/(\d{4,5})', 'lab.views.list_former'),
    url(r'^people/graduate/(PHD|Master)', 'lab.views.list_graduate'),
    url(r'^people/collaborators', 'lab.views.list_collaborators'),
    url(r'^research', 'lab.views.list_research_fields'),
    url(r'^admin/', include(admin.site.urls)),
)
