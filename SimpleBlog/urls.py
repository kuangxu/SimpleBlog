from django.conf.urls import patterns, include, url
from SimpleBlog.blog import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index),
    url(r'^post/(?P<slug>[\w\-]+)$', views.post),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
)
