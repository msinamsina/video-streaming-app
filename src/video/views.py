from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from video.models import Video


# Create your views here.
def video_list(request):
    """View to list all videos."""
    videos = Video.objects.all()
    return render(request, "video/video_list.html", {"videos": videos})


def video_detail(request, video_id):
    """View to display a single video."""
    video = Video.objects.get(id=video_id)
    hls_url = reverse("serve_hls_playlist", args=[video_id])

    return render(request, "video/video_player.html", {"video": video, "hls_url": hls_url})


def serve_hls_playlist(request, video_id):
    """View to serve HLS playlist for a video."""
    video = Video.objects.get(id=video_id)
    hls_playlist_path = video.hls_path

    with open(hls_playlist_path, "r") as m3u8_file:
        m3u8_content = m3u8_file.read()

    base_url = request.build_absolute_uri("/")
    serve_hls_segment_url = f"{base_url}media/videos/hls/{video_id}_{video.name}/"
    m3u8_content = m3u8_content.replace("{{ dynamic_base_url }}", serve_hls_segment_url)

    return HttpResponse(m3u8_content, content_type="application/vnd.apple.mpegurl")
