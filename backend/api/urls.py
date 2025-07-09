from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VideoListCreateView,
    VideoDetailView,
    like_video,
    dislike_video,
    CommentListCreateView,
    WatchLaterListCreateView,
    PlaylistViewSet,
)

router = DefaultRouter()
router.register(r'playlists', PlaylistViewSet, basename='playlist')

urlpatterns = [
    # Video List + Upload
    path('videos/', VideoListCreateView.as_view(), name='video-list-create'),

    #  Video Detail (and auto view count)
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),

    #  Like /  Dislike
    path('videos/<int:video_id>/like/', like_video, name='like-video'),
    path('videos/<int:video_id>/dislike/', dislike_video, name='dislike-video'),

    #  Comments (GET, POST)
    path('videos/<int:video_id>/comments/', CommentListCreateView.as_view(), name='video-comments'),

    #  Watch Later
    path('watchlater/', WatchLaterListCreateView.as_view(), name='watch-later'),
    
    path('upload/', VideoListCreateView.as_view(), name='video-upload'),

    #  Playlists (via ViewSet)
    path('', include(router.urls)),
]
