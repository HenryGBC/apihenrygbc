from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api import views
urlpatterns = [
    #Functions Views
    #url(r'^blog/$', views.blog_list),
    #url(r'^blog/(?P<pk>[0-9]+)/$', views.blog_entry_detail),
    url(r'^blog/$', views.BlogListView.as_view()),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.BlogEntryDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

