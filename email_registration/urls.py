from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'email_registration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include("pages.urls", namespace="pages")),
]

urlpatterns += patterns(
    '',
    url(r'^registration/', include('registration.backends.default.urls')),
)
