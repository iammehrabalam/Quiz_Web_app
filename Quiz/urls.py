from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quizapp.views.home', name='home'),
    url(r'^keepcalm/$', 'quizapp.views.keepcalm', name='keepcalm'),
    url(r'^marking/$', 'quizapp.views.marking', name='marking'),
    url(r'^rules/$', 'quizapp.views.rules', name='rules'),
    url(r'^screening/(?P<ans>\w+)/(?P<qno>\d+)/$', 'quizapp.views.screening', name='screening'),
    # url(r'^$', 'quizapp.views.welcome', name='welcome'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
