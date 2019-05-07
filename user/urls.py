from django.conf.urls import url

from . import views

app_name = "user"

urlpatterns = [
    url(r'test/$', views.test_user, name='test_user'),
]
