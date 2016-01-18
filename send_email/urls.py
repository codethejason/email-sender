from django.conf.urls import url

from . import views

app_name = 'send_email'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^done', views.done, name='done'),
]
