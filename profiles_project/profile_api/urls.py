from django.urls import path, include
from .views import HelloAPIView, HelloViewSet, UserProfileViewSet, UserLoginAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('my', HelloViewSet, basename='hello_name')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('', HelloAPIView.as_view()),
    path('', include(router.urls)),
    path('login/', UserLoginAPIView.as_view())
]
