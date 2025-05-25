from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonationPlatformViewSet, DonationView

router = DefaultRouter()
router.register(r'platforms', DonationPlatformViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('donate/', DonationView.as_view(), name='donate'),
] 