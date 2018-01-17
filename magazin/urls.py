from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^api/', include('root_app.urls_api', namespace='root_app')),
    url(r'^api-token-auth/', obtain_jwt_token),    
    url(r'^', include('root_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
