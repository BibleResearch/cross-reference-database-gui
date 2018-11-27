from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='base'),
    url(r'^api/v1/', include('api.urls')),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^crossrefs/', include('cross_referencer.urls')),
]
