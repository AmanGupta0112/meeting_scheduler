from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingViewSet, MeetingRoomViewSet

router = DefaultRouter()
router.register(r"meetings", MeetingViewSet)
router.register(r"rooms", MeetingRoomViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
