from django.urls import include, path
#from application import views
from django.conf.urls.static import static
from django.conf import settings

from .views import *

'''urls for api'''
urlpatterns = [
    path('', RestaurantListApiView.as_view(), name='list'),
    path('<pk>', RestaurantDetailView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
