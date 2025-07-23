from django.shortcuts import render

from video.models import Video


# Create your views here.
def video_list(request):
    """View to list all videos."""
    videos = Video.objects.all()
    return render(request, "video/video_list.html", {"videos": videos})
