#PODOPIECZNI URLS

from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve
app_name = 'podopieczni'

urlpatterns = [
    url(r'^$',views.ListPodopieczni.as_view(),name='all'),
    url(r'^new/$',views.CreatePodopieczny.as_view(),name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.SinglePodopieczny.as_view(),name='single'),
    url(r'join/(?P<slug>[-\w]+)/$',views.JoinPodopieczny.as_view(),name='join'),
    url(r'leave/(?P<slug>[-\w]+)/$',views.LeavePodopieczny.as_view(),name='leave'),


]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve, {'document_root':settings.MEDIA_ROOT,}),
    ]
