from django.conf.urls import include, url
from blog.api import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'apihenrygbc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/$', views.blog_list),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.blog_entry_detail),
]
