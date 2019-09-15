"""URLs to run the tests."""
from django.conf.urls import include, re_path
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()


urlpatterns = [
    re_path(r'^index/test/$', lambda x: HttpResponse('Success'), name='index'),
    re_path(r'^admin-.+/', include(admin.site.urls)),
    re_path(r'^', include('django_libs.tests.test_app.urls')),
]
