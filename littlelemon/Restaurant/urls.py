from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('booking/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]