from django.conf.urls import include, url
from blog.api import views
urlpatterns = [
    #Functions Views
    #url(r'^blog/$', views.blog_list),
    #url(r'^blog/(?P<pk>[0-9]+)/$', views.blog_entry_detail),
    url(r'^blog/$', views.BlogListView.as_view()),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.BlogEntryDetail.as_view()),
]
