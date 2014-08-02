from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KISS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'slides.views.index', name='index'),
    url(r'^select/$', 'slides.views.screens', name='screens'),
    url(r'^screen/(?P<screen>\d+)$', 'slides.views.screen', name='screen'),
)

