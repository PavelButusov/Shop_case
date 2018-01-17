from django.conf import settings
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^catalogue/$', views.catalogue, name='catalogue'),
    url(r'^to_basket/(?P<product_id>[0-9]+)/$', views.to_basket, name='to_basket'),
    url(r'^cleanup_basket/$', views.cleanup_basket, name='cleanup_basket'),
    url(r'^basket/$', views.basket, name='basket'),
    url(r'^card/(?P<product_id>[0-9]+)/$', views.card, name='card'),
] 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
