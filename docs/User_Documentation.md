# Livestream App User Documentation

## Overview
The Livestream App allows you to stream RTSP video feeds with custom overlays. You can add text and image overlays that appear on top of the video stream, and manage them through a user-friendly interface.

## Prerequisites

### System Requirements
- Python 3.8 or higher
- Node.js 14 or higher
- MongoDB 4.4 or higher
- OpenCV compatible system

### Required Software
1. **MongoDB**: Download and install from [mongodb.com](https://www.mongodb.com/try/download/community)
2. **Python**: Download from [python.org](https://www.python.org/downloads/)
3. **Node.js**: Download from [nodejs.org](https://nodejs.org/)

## Installation and Setup

### 1. Clone or Extract the Project
Extract the project files to your desired location.

### 2. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start MongoDB service:
   - On Windows: MongoDB should start automatically if installed as a service
   - On macOS/Linux: `sudo systemctl start mongod` or `brew services start mongodb-community`

5. Configure environment variables (optional):
   - Edit the `.env` file to change database settings if needed
   - Default settings work for local development

6. Start the backend server:
   ```bash
   python app.py
   ```

The backend server will start on `http://localhost:5000`

### 3. Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The frontend will start on `http://localhost:3000` and automatically open in your browser.

## Using the Application

### 1. Starting a Livestream

1. **Enter RTSP URL**: In the video player section, enter a valid RTSP URL in the input field.

   **Sample RTSP URLs for testing:**
   - `rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov`
   - `rtsp://rtsp.stream/pattern`

2. **Click Play**: Click the "Play" button to start streaming.

3. **Volume Control**: Use the volume slider to adjust audio levels.

4. **Stop Stream**: Click "Stop" to end the stream.

### 2. Managing Overlays

#### Creating a New Overlay

1. Click "Add New Overlay" in the Overlay Manager section.

2. Fill in the overlay details:
   - **Name**: A descriptive name for your overlay
   - **Type**: Choose "Text" for text overlays or "Image" for image overlays
   - **Content**: 
     - For text overlays: Enter the text you want to display
     - For image overlays: Enter the URL of the image
   - **Position**: Set X and Y coordinates (in pixels) for overlay placement
   - **Size**: Set width and height (in pixels) for the overlay

3. Click "Create" to save the overlay.

#### Editing an Overlay

1. In the "Existing Overlays" list, click "Edit" next to the overlay you want to modify.

2. Update the desired fields in the form.

3. Click "Update" to save changes.

#### Deleting an Overlay

1. In the "Existing Overlays" list, click "Delete" next to the overlay you want to remove.

2. Confirm the deletion in the popup dialog.

### 3. Overlay Types

#### Text Overlays
- Display custom text on the video
- Appear with a semi-transparent black background for readability
- Font size is fixed at 16px
- Color is white for visibility

#### Image Overlays
- Display images from URLs
- Support common image formats (PNG, JPG, GIF)
- Images are scaled to fit the specified size
- Transparent backgrounds are supported

### 4. Positioning Overlays

- **X Position**: Distance from the left edge of the video (in pixels)
- **Y Position**: Distance from the top edge of the video (in pixels)
- **Width**: Overlay width (in pixels)
- **Height**: Overlay height (in pixels)

**Tips for positioning:**
- Start with small values (10-50) for positions near edges
- For center positioning, use approximately half the video width/height
- Test different positions to find the best placement

## Troubleshooting

### Common Issues

#### 1. Stream Won't Start
- **Check RTSP URL**: Ensure the URL is valid and accessible
- **Network Issues**: Verify internet connection and firewall settings
- **RTSP Server**: Confirm the RTSP server is running and accessible

#### 2. Overlays Not Appearing
- **Check Overlay Settings**: Verify position and size values are reasonable
- **Image URLs**: For image overlays, ensure URLs are accessible and point to valid images
- **Browser Cache**: Try refreshing the page or clearing browser cache

#### 3. Backend Connection Issues
- **Server Status**: Ensure the backend server is running on port 5000
- **CORS Issues**: The backend includes CORS headers, but check browser console for errors
- **Database Connection**: Verify MongoDB is running and accessible

#### 4. Performance Issues
- **Video Quality**: High-resolution streams may cause performance issues
- **Multiple Overlays**: Too many overlays can impact performance
- **Browser Resources**: Close unnecessary browser tabs and applications

### Error Messages

#### "Failed to start stream"
- The RTSP URL is invalid or inaccessible
- Check the URL format and network connectivity

#### "Overlay not found"
- Trying to edit/delete a non-existent overlay
- Refresh the page to sync with the database

#### "Missing required fields"
- Form submission with incomplete data
- Ensure all required fields are filled

## Advanced Configuration

### Environment Variables

Edit the `backend/.env` file to customize:

```
MONGODB_URI=mongodb://localhost:27017/
DB_NAME=livestream_db
FLASK_ENV=development
PORT=5000
```

### Database Configuration

The app uses MongoDB with the following collections:
- `overlays`: Stores overlay configurations

### RTSP Stream Sources

#### Free Test Streams
- Wowza Demo: `rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov`
- RTSP.stream: `rtsp://rtsp.stream/pattern`

#### Creating Your Own RTSP Stream
1. Use OBS Studio with RTSP output plugin
2. Use VLC Media Player to stream files via RTSP
3. Use IP cameras with RTSP support
4. Use services like RTSP.me for temporary streams

## API Integration

The application provides REST APIs for programmatic access. See `API_Documentation.md` for detailed endpoint information.

## Support and Maintenance

### Logs
- Backend logs appear in the terminal where you started the Flask server
- Frontend logs appear in the browser's developer console

### Database Management
- Use MongoDB Compass for visual database management
- Connect to `mongodb://localhost:27017/livestream_db`

### Updates
- Backend: Update Python packages with `pip install -r requirements.txt --upgrade`
- Frontend: Update Node packages with `npm update`

## Security Considerations

- The application is designed for local development
- For production deployment, implement authentication and HTTPS
- Validate all RTSP URLs and image URLs for security
- Consider rate limiting for API endpoints