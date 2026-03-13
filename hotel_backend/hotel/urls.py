from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewset, BookingViewset, RoomViewset

router = DefaultRouter()
router.register('customer', CustomerViewset)
router.register('booking', BookingViewset)
router.register('room', RoomViewset)

urlpatterns = [
    path('', include(router.urls))

]