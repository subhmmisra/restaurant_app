from django.contrib import admin
from django.urls import path, include
from application.urls import *
'''url register to main project'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('application.api.urls')),
]
