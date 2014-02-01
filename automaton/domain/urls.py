from django.conf.urls import patterns, include, url

urlpatterns = patterns('domain.views',
    # Examples:
    # url(r'^$', 'automaton.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^oauth2callback$', 'callback_auth', name="auth_callback"),
    url(r'^login$', 'init_auth', name="login"),
    url(r'^$', "home", name="home")
)