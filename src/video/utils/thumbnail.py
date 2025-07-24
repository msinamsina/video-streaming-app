import os
import subprocess


def generate_thumbnail(video_path, thumbnail_path, time="00:00:01"):
    """
    Generate a thumbnail for a video at a specific time using ffmpeg.

    :param video_path: Path to the video file.
    :param thumbnail_path: Path where the thumbnail will be saved.
    :param time: Time in the video to capture the thumbnail (default is 1 second).
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file {video_path} does not exist.")

    # Ensure the directory for the thumbnail exists
    os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
    if os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)  # Remove existing thumbnail if it exists

    # generate thumbnail
    command = ["ffmpeg", "-i", video_path, "-ss", "2", "-vframes", "1", "-q:v", "2", "-y", thumbnail_path]
    subprocess.run(command, check=True)
    if not os.path.exists(thumbnail_path):
        raise RuntimeError(f"Failed to create thumbnail at {thumbnail_path}.")
