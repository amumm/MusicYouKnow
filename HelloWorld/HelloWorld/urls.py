from django.conf.urls import include, url
from HelloWorldApp.views import music, music3

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = (

    url(r'song/$', music),
    url(r'song/(?P<year>\d{4})/$', music3),
)
