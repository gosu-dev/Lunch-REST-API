from datetime import datetime

from rest_framework import generics, viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Restaurant, Menu, Dish
from .serializers import RestaurantSerializer, MenuSerializer, DishSerializer


class RestaurantViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


class MenuViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=False)
        if len(request.data) != 7:
            return Response('There should be a menu for each day',
                            status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def list(self, request):
        today = datetime.today().weekday() + 1
        queryset = self.get_queryset().filter(weekday=today)
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)


class DishViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantAPICreate(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
