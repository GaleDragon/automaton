from django.conf.urls import patterns, include, url
__author__ = 'jeremymorgan'

urlpatterns = patterns('runner.views',
    # Examples:
    # url(r'^$', 'automaton.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'start$', 'runner_view', name="start"),
    url(r'(?P<index>\d+)/results', 'results', name="results"),
)