# coding:utf-8
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from djblog.blog.feeds import LatestPostFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'djblog.views.handler404'
handler500 = 'djblog.views.handler500'

urlpatterns = patterns('',
    (r'^$', 'djblog.views.home'),
	(r'^archives/$', 'djblog.views.archives'),
    (r'^admin/', include(admin.site.urls)),
	(r'^static/(?P<path>.*)$', 'djblog.static.serve', {'document_root': settings.STATIC_ROOT,}), # TODO 用nginx配置代替
)

# blogs
urlpatterns += patterns('djblog.blog.views',
	(r'^post/(?P<pid>\d+)/', 'show_post'),
	(r'^tag/(?P<name>.+)/$', 'list_by_tag'),
    (r'^feed/$', LatestPostFeed()),
)
