from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout$', views.checkout_page),
    url(r'^checkout/process$', views.checkout)
]