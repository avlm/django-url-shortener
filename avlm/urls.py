from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^shortener$', views.shortener, name='shortener'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^sign_up$', views.sign_up, name='sign_up'),
    url(r'^login$', views.sign_in, name='login'),
    url(r'^(?P<param_hash>([A-Z]|[a-z]|[0-9])+)$', views.redirect, name='redirect'),
]
