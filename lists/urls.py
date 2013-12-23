from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(.+)/$',         'lists.views.view_list', name='view_list'),
    url(r'^new$',           'lists.views.new_list',  name='new_list'),
)
