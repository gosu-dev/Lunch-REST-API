from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from employee.views import EmployeeViewSet, VoteViewSet
from restaurant.views import RestaurantAPICreate, RestaurantViewSet, \
    MenuViewSet, DishViewSet

router = routers.DefaultRouter()
router.register(r'restaurant', RestaurantViewSet, basename='restaurant')
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'dish', DishViewSet, basename='dish')
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'vote', VoteViewSet, basename='vote')


# router.register(r'restaurant', RestaurantAPICreate)
# router.register()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
