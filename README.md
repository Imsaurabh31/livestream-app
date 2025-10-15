# Livestream App with RTSP Support

A full-stack application for streaming RTSP video feeds with customizable overlays.

## Features

- **RTSP Video Streaming**: Stream live video from RTSP URLs
- **Custom Overlays**: Add text and image overlays on top of video streams
- **Real-time Controls**: Play, pause, and volume adjustment
- **CRUD API**: Complete REST API for overlay management
- **Responsive UI**: Modern React-based user interface
- **MongoDB Storage**: Persistent overlay configuration storage

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: React.js
- **Database**: MongoDB
- **Video Processing**: OpenCV
- **Styling**: CSS3

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- MongoDB 4.4+

### Installation

1. **Backend Setup**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

2. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   npm start
   ```

3. **Access the App**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

## Project Structure

```
Livestream/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt       # Python dependencies
│   ├── config/
│   │   └── database.py       # MongoDB configuration
│   ├── models/
│   │   └── overlay.py        # Overlay data model
│   └── routes/
│       ├── overlay_routes.py # Overlay CRUD endpoints
│       └── stream_routes.py  # Streaming endpoints
├── frontend/
│   ├── package.json          # Node.js dependencies
│   ├── src/
│   │   ├── App.js           # Main React component
│   │   ├── components/
│   │   │   ├── VideoPlayer.js    # Video streaming component
│   │   │   └── OverlayManager.js # Overlay management UI
│   │   └── services/
│   │       └── api.js       # API service layer
│   └── public/
│       └── index.html       # HTML template
└── docs/
    ├── API_Documentation.md  # API reference
    └── User_Documentation.md # User guide
```

## Usage

1. **Start Streaming**: Enter an RTSP URL and click "Play"
2. **Add Overlays**: Use the Overlay Manager to create text or image overlays
3. **Position Overlays**: Set custom positions and sizes for overlays
4. **Manage Overlays**: Edit or delete existing overlays as needed

## Sample RTSP URLs

- `rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov`
- `rtsp://rtsp.stream/pattern`

## API Endpoints

- `POST /api/overlays` - Create overlay
- `GET /api/overlays` - Get all overlays
- `GET /api/overlays/{id}` - Get overlay by ID
- `PUT /api/overlays/{id}` - Update overlay
- `DELETE /api/overlays/{id}` - Delete overlay
- `POST /api/stream/start` - Start RTSP stream
- `POST /api/stream/stop` - Stop stream
- `GET /api/stream/video` - Video feed endpoint

## Documentation

- [API Documentation](docs/API_Documentation.md)
- [User Documentation](docs/User_Documentation.md)

## License

This project is open source and available under the MIT License.