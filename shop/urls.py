from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='shop.views.index'),
    url(r'^search/$', views.search, name='shop.views.search'),
]