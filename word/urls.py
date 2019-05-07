from django.conf.urls import url

from . import views

app_name = "word"

urlpatterns = [
    url(r'^test/$', views.test_word, name='test_word'),
]
