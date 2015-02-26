'''
  The page heirarchy of the webapp is as follows:
  
                   iLabelIT
                   /      \
                 Login  Signup
                 /   \
               Quiz  Annotation
                

'''

from django.conf.urls import patterns, include, url
from django.contrib import admin

import retinalwebapp.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'retinalwebapp.views.home', name='home'),
    url(r'^signup', 'retinalwebapp.views.signup', name='signup'),
    url(r'^choose_activity', 'retinalwebapp.views.choose_activity', name='choose_activity'),
    url(r'^annotation', 'retinalwebapp.views.annotation', name='annotation'), 
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # user auth urls
    url(r'^accounts/login/$', 'retinalwebapp.views.login'),
    url(r'^accounts/auth/$', 'retinalwebapp.views.auth_views'),
    # url(r'^accounts/logout/$', 'retinalwebapp.views.logout'),
    url(r'^accounts/loggedin/$', 'retinalwebapp.views.loggedin'),
    url(r'^accounts/invalid/$', 'retinalwebapp.views.invalid_login'),
   # url(r'^accounts/register/$', 'retinalwebapp.views.register_user'),
    #url(r'^accounts/register_success/$', 'retinalwebapp.views.register_success'),
)
