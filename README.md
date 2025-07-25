# 🎬 Pomegranate Video Streaming App

<div align="center">

![Pomegranate Video Streaming App Banner](./assets/pomegranate-banner.svg)

[![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

A modern Django-based video streaming application that provides HLS (HTTP Live Streaming) video playback with automatic video conversion, thumbnail generation, and a responsive web interface.deo Streaming App


## Demo
### Video List Demo

<div align="center">
   <img src="./assets/video_list.JPG" alt="Video Player Interface" width="80%" />
   <p><i>Clean and organized video library interface for easy browsing</i></p>
</div>

### Video Player Demo

<div align="center">
   <img src="./assets/video_player.JPG" alt="Video Player Interface" width="80%" />
   <p><i>The responsive Video.js player with HLS streaming</i></p>
</div>


### Mobile Experience

<div align="center">
   <img src="./assets/video_player_mobile.JPG" alt="Mobile Interface" width="40%" />
   <p><i>Responsive design for mobile devices</i></p>
</div>

## ✨ Features

- **Video Upload & Management**: Upload videos in various formats with automatic conversion
- **HLS Streaming**: Adaptive bitrate streaming using HLS protocol for optimal viewing experience
- **Automatic Processing**:
  - Video conversion to HLS format using FFmpeg
  - Thumbnail generation from video frames
  - Duration extraction
- **Responsive UI**: Modern, mobile-friendly interface with Video.js player
- **Admin Interface**: Django admin integration for video management
- **Docker Support**: Containerized deployment with Docker
- **Dev Container**: VS Code dev container support for development

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Video Processing**: FFmpeg
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Video Player**: Video.js with HLS support
- **Image Processing**: Pillow
- **Containerization**: Docker

## 📁 Project Structure

```
video-streaming-app/
├── src/
│   ├── pomegranate/           # Django project settings
│   ├── video/                 # Main video app
│   │   ├── models.py         # Video model
│   │   ├── views.py          # Video views
│   │   ├── signals.py        # Post-save processing
│   │   └── utils/            # Video processing utilities
│   │       ├── convert.py    # HLS conversion
│   │       └── thumbnail.py  # Thumbnail generation
│   ├── templates/            # HTML templates
│   └── media/               # User uploads & processed files
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
└── dev-compose.yml         # Development docker-compose
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- FFmpeg
- Docker (optional)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/msinamsina/video-streaming-app.git
   cd video-streaming-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**
   - **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Windows**: Download from [FFmpeg official website](https://ffmpeg.org/download.html)

5. **Run migrations**
   ```bash
   cd src
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main app: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

### Docker Development

1. **Using Docker Compose**
   ```bash
   docker-compose -f dev-compose.yml up --build
   ```

2. **Access the application**
   - Application: http://localhost:8000

## 📋 Usage

### Uploading Videos

1. Access the Django admin panel at `/admin`
2. Navigate to Videos section
3. Click "Add Video" and upload your video file
4. The system will automatically:
   - Convert the video to HLS format
   - Generate a thumbnail
   - Extract video duration
   - Create streaming segments

### Viewing Videos

1. Visit the main page to see all uploaded videos
2. Click on any video to open the video player
3. The player supports:
   - HLS adaptive streaming
   - Full-screen mode
   - Playback controls
   - Mobile-responsive design

## ⚙️ Configuration

### Settings

Key settings in `src/pomegranate/settings.py`:

```python
# Media files configuration
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Video processing settings can be customized in:
# - src/video/utils/convert.py (HLS conversion parameters)
# - src/video/utils/thumbnail.py (thumbnail generation)
```

### Video Processing Options

Customize video processing in `src/video/utils/convert.py`:

- **HLS Segment Duration**: Default 10 seconds
- **Video Codec**: Copy (no re-encoding for faster processing)
- **Audio Codec**: Copy
- **Hardware Acceleration**: Auto-detected

## 🔧 API Endpoints

- `GET /` - Video list page
- `GET /video/<id>/` - Video player page
- `GET /video/<id>/hls/` - HLS playlist endpoint
- `GET /media/videos/hls/<id>/` - HLS segments

## 🐛 Troubleshooting

### Common Issues

1. **FFmpeg not found**
   - Ensure FFmpeg is installed and available in PATH
   - On Docker: FFmpeg is included in the container

2. **Video upload fails**
   - Check file size limits in Django settings
   - Verify media directory permissions

3. **HLS streaming not working**
   - Ensure Video.js and HLS.js are properly loaded
   - Check browser console for JavaScript errors

### Debug Mode

Enable debug mode in settings for detailed error messages:
```python
DEBUG = True
```

## 🔒 Security Considerations

- The current configuration uses `DEBUG = True` and a development secret key
- For production deployment:
  - Set `DEBUG = False`
  - Use a secure `SECRET_KEY`
  - Configure `ALLOWED_HOSTS`
  - Use a production database (PostgreSQL recommended)
  - Set up proper media file serving (nginx, CDN)

## 🚀 Production Deployment

### Environment Variables

Create a `.env` file for production:
```env
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost/dbname
ALLOWED_HOSTS=your-domain.com
```

### Docker Production

1. Build production image:
   ```bash
   docker build -t video-streaming-app .
   ```

2. Run with environment variables:
   ```bash
   docker run -p 8000:8000 --env-file .env video-streaming-app
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **msinamsina** - *Initial work* - [GitHub](https://github.com/msinamsina)

## 🙏 Acknowledgments

- [Django](https://djangoproject.com/) - Web framework
- [FFmpeg](https://ffmpeg.org/) - Video processing
- [Video.js](https://videojs.com/) - HTML5 video player
- [Bootstrap](https://getbootstrap.com/) - CSS framework

## 📊 Performance Notes

- Videos are processed asynchronously after upload
- HLS segments are generated for adaptive streaming
- Thumbnails are extracted at the 2-second mark
- Hardware acceleration is used when available

## 🔮 Future Enhancements

- [ ] Multiple video quality options
- [ ] User authentication and playlists
- [ ] Video analytics and statistics
- [ ] Subtitle support
- [ ] Live streaming capabilities
- [ ] CDN integration
- [ ] Advanced video player features
