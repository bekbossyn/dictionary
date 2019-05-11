from django.conf.urls import url

from . import views

app_name = "word"

urlpatterns = [
    url(r'^test/$', views.test_word, name='test_word'),
    url(r'^test_show_word/$', views.test_show_word, name='test_show_word'),
    url(r'^languages/$', views.languages, name='languages'),
]
