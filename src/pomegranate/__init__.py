"""Pomegranate: A Django application for video uploading and HLS streaming.

This package provides the core functionality for a video-on-demand platform.
It allows users to upload video files, which are then processed and made
available for streaming using the HTTP Live Streaming (HLS) protocol.

Key Features:
-   **Video Upload:** A simple interface for users to upload video files.
-   **Video Listing:** A view that displays a list of all processed and
    available videos.
-   **HLS Streaming:** A dedicated player page for each video that serves
    the content using an HLS manifest, enabling adaptive bitrate streaming.

This app is designed to be integrated into a larger Django project, handling
the backend logic for video management and delivery.
"""
