from django.conf.urls import url, patterns


urlpatterns = patterns(
    'pages.views',
    url(r'^$', 'index_view', name="index")
)
