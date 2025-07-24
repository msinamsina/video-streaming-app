# import post_save
from django.db.models.signals import post_save
from django.dispatch import receiver

from video.models import Video
from video.utils import get_video_duration
from video.utils.convert import convert_to_hls
from video.utils.thumbnail import generate_thumbnail


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        video_path = instance.file.path
        thumbnail_path = f"./media/thumbnails/{instance.id}_{instance.name}.jpg"
        generate_thumbnail(video_path, thumbnail_path)
        instance.thumbnail = f"thumbnails/{instance.id}_{instance.name}.jpg"
        instance.duration = get_video_duration(video_path)
        instance.save()  # Save the instance to update the thumbnail
        # Logic to execute after a Video instance is created
        output_dir = f"./media/videos/hls/{instance.id}_{instance.name}"
        instance.hls_path = convert_to_hls(video_path, output_dir)
        instance.save()  # Save the instance to update the hls_path
        # Additional logic can be added here, such as logging or notifications
        print(f"Video created: {instance.name}")
    else:
        # Logic to execute after a Video instance is updated
        print(f"Video updated: {instance.name}")
