from django.conf.urls import url

from . import views

app_name = 'cross_referencer'
urlpatterns = [
    url(r'^$', views.CrossReferenceListView.as_view(), name='list'),
    url(r'^new/$', views.CrossReferenceCreateView.as_view(), name='new'),
    url(r'^(?P<pk>[0-9a-f]{1,})/$', views.CrossReferenceDetailView.as_view(), name='details'),
    url(r'^(?P<pk>[0-9a-f]{1,})/edit', views.CrossReferenceEditView.as_view(), name='edit'),
    url(r'^(?P<pk>[0-9a-f]{1,})/delete', views.CrossReferenceDeleteView.as_view(), name='delete'),
]
