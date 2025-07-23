from django.urls import path

from video.views import video_list

urlpatterns = [
    path("", video_list, name="video_list"),
]
