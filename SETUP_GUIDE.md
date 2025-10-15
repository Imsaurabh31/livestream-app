# Livestream App - Complete Setup Guide

## 🚀 Quick Start (Windows)

### Option 1: Automatic Setup
1. Double-click `start_app.bat` to automatically start both servers
2. The app will open at http://localhost:3000

### Option 2: Manual Setup

#### Step 1: Install Prerequisites
1. **Python 3.8+**: Download from https://python.org
2. **Node.js 14+**: Download from https://nodejs.org
3. **MongoDB**: Download from https://mongodb.com/try/download/community

#### Step 2: Start MongoDB
- MongoDB should start automatically if installed as a service
- Or manually start: `mongod`

#### Step 3: Start Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Step 4: Start Frontend
```bash
cd frontend
npm install
npm start
```

## 📁 Project Structure Overview

```
Livestream/
├── 🖥️ backend/           # Python Flask API server
├── 🌐 frontend/          # React.js web application  
├── 📚 docs/              # Documentation files
├── 🚀 start_app.bat      # Quick startup script
└── 📖 README.md          # Project overview
```

## 🎯 Key Features Implemented

✅ **RTSP Video Streaming**
- Real-time video streaming from RTSP URLs
- Play/pause/stop controls
- Volume adjustment

✅ **Custom Overlays**
- Text overlays with custom positioning
- Image overlays from URLs
- Drag-and-drop positioning (via form inputs)
- Resizable overlays

✅ **CRUD API for Overlays**
- Create new overlays
- Read/retrieve all overlays
- Update existing overlays
- Delete overlays

✅ **Modern UI**
- Responsive React interface
- Real-time overlay preview
- User-friendly overlay management

✅ **Database Storage**
- MongoDB for persistent overlay storage
- Automatic timestamps for created/updated dates

## 🔧 Testing the Application

### 1. Test RTSP Streaming
Use these sample RTSP URLs:
- `rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov`
- `rtsp://rtsp.stream/pattern`

### 2. Test Overlay Creation
1. Create a text overlay:
   - Name: "Sample Text"
   - Type: Text
   - Content: "Hello World!"
   - Position: X=50, Y=50
   - Size: 200x50

2. Create an image overlay:
   - Name: "Logo"
   - Type: Image
   - Content: "https://via.placeholder.com/100x50/0000FF/FFFFFF?text=LOGO"
   - Position: X=10, Y=10
   - Size: 100x50

### 3. Test API Endpoints
Use tools like Postman or curl to test:
- GET http://localhost:5000/api/overlays
- POST http://localhost:5000/api/overlays
- PUT http://localhost:5000/api/overlays/{id}
- DELETE http://localhost:5000/api/overlays/{id}

## 🛠️ Troubleshooting

### Common Issues:

**"Module not found" errors:**
- Run `pip install -r requirements.txt` in backend folder
- Run `npm install` in frontend folder

**MongoDB connection errors:**
- Ensure MongoDB is installed and running
- Check if port 27017 is available

**RTSP stream not loading:**
- Try different RTSP URLs
- Check internet connection
- Some RTSP streams may have access restrictions

**Port already in use:**
- Backend (5000): Change PORT in backend/.env
- Frontend (3000): React will automatically suggest alternative port

## 📋 Development Notes

### Backend Architecture:
- **Flask**: Web framework
- **OpenCV**: Video processing
- **PyMongo**: MongoDB integration
- **Flask-CORS**: Cross-origin requests

### Frontend Architecture:
- **React**: UI framework
- **Axios**: HTTP client
- **CSS3**: Styling

### Database Schema:
```javascript
// Overlay Document
{
  _id: ObjectId,
  name: String,
  type: "text" | "image",
  content: String,
  position: { x: Number, y: Number },
  size: { width: Number, height: Number },
  created_at: Date,
  updated_at: Date
}
```

## 🚀 Production Deployment

For production deployment, consider:
1. Use environment variables for configuration
2. Implement authentication and authorization
3. Use HTTPS for secure connections
4. Set up proper error logging
5. Use a production WSGI server (e.g., Gunicorn)
6. Use a production web server (e.g., Nginx)
7. Set up MongoDB with proper security

## 📞 Support

If you encounter any issues:
1. Check the console logs (browser and terminal)
2. Verify all prerequisites are installed
3. Ensure MongoDB is running
4. Check firewall settings for ports 3000, 5000, and 27017

## 🎉 Success!

If everything is working correctly, you should see:
- Backend server running on http://localhost:5000
- Frontend app running on http://localhost:3000
- Ability to stream RTSP videos
- Ability to create and manage overlays
- Overlays appearing on top of video streams