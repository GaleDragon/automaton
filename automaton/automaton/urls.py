from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'automaton.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('domain.urls')),
    url(r'^runner/', include('runner.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
