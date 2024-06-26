from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,MenuItemsView, SingleMenuItemView,BookingViewSet

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'booking', BookingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu-items/', MenuItemsView.as_view(), name='menu-list'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
]