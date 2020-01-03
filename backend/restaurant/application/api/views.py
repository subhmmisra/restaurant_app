from rest_framework.generics import ListAPIView, RetrieveAPIView
from application.models import *
from .serializers import *
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter

'''views for api'''


class RestaurantListApiView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    filter_backends = (SearchFilter, OrderingFilter)

    def get_queryset(self, *args, **kwargs):
        query_list = Restaurant.objects.all()
        query = self.request.GET.get("q")
        if query:
            query_list = query_list.filter(
                Q(cuisines__icontains=query)
            ).distinct()
        return query_list


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
