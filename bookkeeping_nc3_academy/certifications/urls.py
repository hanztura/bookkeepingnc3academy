from django.conf.urls import url

from . import views

app_name = 'certifications'
urlpatterns = [
    url(r'^topics/(?P<id>[0-9]+)/$', views.TopicViews.detail, name='topic_detail'),
    url(r'^topics/(?P<id>[0-9]+)/update/', views.TopicViews.update, name='topic_update'),
]