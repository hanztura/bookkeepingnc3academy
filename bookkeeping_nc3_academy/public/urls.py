from django.conf.urls import url

from . import views

app_name = 'public'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^forms/pass_nc3/', views.form_mail, name='form_mail'),
]