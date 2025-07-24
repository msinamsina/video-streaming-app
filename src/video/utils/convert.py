import os
import subprocess


def convert_to_mp4(input_file, output_file):
    """
    Convert a video file to MP4 format using FFmpeg.

    Args:
        input_file (str): Path to the input video file.
        output_file (str): Path where the converted MP4 file will be saved.
    """
    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-c:v",
        "libx264",
        "-c:a",
        "aac",
        "-strict",
        "experimental",
        "-b:a",
        "192k",
        output_file,
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


def convert_to_hls(input_file, output_dir):
    """
    Convert a video file to HLS format using FFmpeg.

    Args:
        input_file (str): Path to the input video file.
        output_dir (str): Directory where the HLS files will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    command = [
        "ffmpeg",
        "-hwaccel",
        "auto",  # Use hardware acceleration if available
        "-i",
        input_file,
        "-preset",
        "ultrafast",  # Fastest encoding preset (larger output, lower CPU)
        "-tune",
        "fastdecode",  # Tune for fast decoding (skip complexity)
        "-g",
        "60",  # Keyframe interval (1 keyframe every 2 sec at 30fps)
        "-sc_threshold",
        "0",  # Disable scene change detection (saves CPU)
        "-f",
        "hls",
        "-c:v",
        "copy",
        "-c:a",
        "copy",
        "-hls_time",
        "10",
        "-hls_list_size",
        "0",  # Include all segments in playlist
        "-hls_segment_filename",
        os.path.join(output_dir, "segment_%03d.ts"),
        "-hls_flags",
        "independent_segments",  # Ensure each segment is independently decodable
        "-hls_base_url",
        "{{ dynamic_base_url }}",
        os.path.join(output_dir, "playlist.m3u8"),
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted {input_file} to HLS format in {output_dir}")
        return os.path.join(output_dir, "playlist.m3u8")
    except subprocess.CalledProcessError as e:
        print(f"Error during HLS conversion: {e}")
