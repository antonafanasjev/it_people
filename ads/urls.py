from django.contrib.auth.views import login, logout
from django.conf.urls import url
from django.contrib import admin
from django.contrib import auth

import editor.views as editor


urlpatterns = [
    url(r'^login/$',                editor.login_view),
    url(r'^logout/$',               auth.views.logout),
    url(r'^ads/create/?$',          editor.new_ad),
    url(r'^ads/?$',                 editor.ads_list),
    url(r'^ad/(?P<id>\d+)/edit/?$', editor.ad_edit),
    url(r'^ad/(?P<id>\d+)/?$',      editor.ad_view)
]
