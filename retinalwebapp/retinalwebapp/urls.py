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
)
