from django.db import models


# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="videos/")
    hls_path = models.CharField(max_length=255, blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)

    def __str__(self):
        return self.name
