from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register('following', FollowViewSet, basename='following')

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls))
]
