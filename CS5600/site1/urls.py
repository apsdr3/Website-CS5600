from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.site1Test, name='site1Test'),
]