from django.urls import path

from video.views import serve_hls_playlist, video_detail, video_list

urlpatterns = [
    path("", video_list, name="video_list"),
    path("<int:video_id>/", video_detail, name="video_detail"),
    path("<int:video_id>/hls/", serve_hls_playlist, name="serve_hls_playlist"),
]
