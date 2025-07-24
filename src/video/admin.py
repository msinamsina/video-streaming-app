from django.contrib import admin

from video.models import Video


# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("name", "uploaded_at", "duration")
    search_fields = ("name", "description")
    list_filter = ("uploaded_at",)
    ordering = ("-uploaded_at",)
    fieldsets = (
        (None, {"fields": ("name", "description", "file", "thumbnail")}),
        ("Advanced options", {"fields": ("hls_path", "duration"), "classes": ("collapse",)}),
    )
