from django.conf.urls.defaults import *
from hierarchies.feeds import CategoryFeed
from hierarchies.models import Category, Hierarchy
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line for to enable the admin:
    (r'^admin/hierarchies/', include('hierarchies.urls.admin')),
    url(r'^admin/alfresco/cache/', 'alfresco.views.cache', name='alfresco_cache'),
    url(r'^admin/(.*)', admin.site.root, name='admin_home'),
    (r'^alfresco/', include('alfresco.urls')),
    (r'^sample_site/', include('sample_site.urls')),
    url(r'^site_map/$', 'django.views.generic.simple.direct_to_template', {
        'template' : 'site_map.html' }, name='site_map'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'sample_site.views.home', name='home'),
    url(r'^(?P<slug>[-\w]+)/$','sample_site.views.hierarchy_detail', 
        {'queryset' : Hierarchy.objects.all(), 'slug_field' : 'slug'}, name='hierarchy_detail'),
    url(r'^(?P<path>.*)/content/(?P<id>[-\w]+)/$$', 'sample_site.views.category_content_detail', name='category_content_detail'),
    url(r'^(?P<path>.*)/$', 'sample_site.views.category_detail', 
        {'queryset' : Category.objects.all(), 'slug_field' : 'slug'}, name='category_detail'),
)