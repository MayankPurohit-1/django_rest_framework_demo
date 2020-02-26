from django.urls import path, include
from .views import HelloAPIView, HelloViewSet, UserProfileViewSet, UserLoginApiView, UserProfileFeedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('my', HelloViewSet, basename='hello_name')
router.register('profile', UserProfileViewSet)
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    path('', HelloAPIView.as_view()),
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),
]
