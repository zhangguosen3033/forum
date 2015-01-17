from django.conf.urls import patterns, include, url
from forum.forms.user import LoginForm

from views import common, user

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xp.views.home', name='home'),
    # url(r'^xp/', include('xp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^setting/$', common.method_splitter, {'GET': user.get_setting, 'POST': user.post_setting}),
    url(r'^setting/avatar/$', common.method_splitter, {'GET': user.get_setting_avatar, 'POST': user.post_setting_avatar}),
    url(r'^setting/password/$', common.method_splitter, {'GET': user.get_settingpwd, 'POST': user.post_settingpwd}),
    url(r'^forgot/$', common.method_splitter, {'GET': user.get_forgotpwd, 'POST': user.post_forgotpwd}),
    url(r'^login/$', common.method_splitter, {'GET': user.get_login, 'POST': user.post_login}),
    url(r'^logout/$', user.get_logout),
    url(r'^register/$', common.method_splitter, {'GET': user.get_register, 'POST': user.post_register}),
)
