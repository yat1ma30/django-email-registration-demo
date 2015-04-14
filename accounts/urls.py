from django.conf.urls import url, patterns

urlpatterns = patterns(
    'accounts.views',
    url(r'^profile/$', 'profile_view', name="profile")
)
