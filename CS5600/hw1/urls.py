from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.hw1, name='hw1'),

    # ex: /hw1/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /hw1/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /hw1/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^hw1/latest\.html$', views.hw1),
]