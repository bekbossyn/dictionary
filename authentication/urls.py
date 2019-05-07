from django.conf.urls import url

from . import views

app_name = "authentication"

urlpatterns = [
    url(r'^test/$', views.test_authentication, name='test_authentication'),
]
