from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (get_confirmation_code, get_token, UserViewSet)

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', get_confirmation_code, name='get_confirmation_code'),
    path('v1/auth/token/', get_token, name='get_jwt_token'),
    path('v1/', include(router_v1.urls)),
]
