# 🔧 Livestream App Troubleshooting Guide

## ❌ "Failed to Live Stream" Error

### **Quick Fix Steps:**

1. **Install Backend Dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Start Backend Server:**
   ```bash
   python app.py
   ```
   Should show: `Running on http://0.0.0.0:5000`

3. **Test RTSP URLs:**
   Use these working URLs:
   - `rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov`
   - `http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4`

### **Common Issues & Solutions:**

#### 🔴 Backend Not Running
**Error:** `Failed to start stream: Network Error`
**Solution:** 
```bash
cd backend
python app.py
```

#### 🔴 OpenCV Not Installed
**Error:** `ModuleNotFoundError: No module named 'cv2'`
**Solution:**
```bash
pip install opencv-python-headless
```

#### 🔴 MongoDB Not Running
**Error:** `pymongo.errors.ServerSelectionTimeoutError`
**Solution:**
- Windows: Start MongoDB service
- Or use MongoDB Atlas (cloud)

#### 🔴 RTSP URL Issues
**Error:** `Failed to connect to RTSP stream`
**Solutions:**
- Try HTTP video URLs instead of RTSP
- Use sample URLs provided in the app
- Check internet connection

### **Alternative Video Sources:**

If RTSP doesn't work, try these HTTP video URLs:
```
http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4
http://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4
https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4
```

### **Test Backend Manually:**

1. **Check if backend is running:**
   Open: http://localhost:5000

2. **Test stream endpoint:**
   ```bash
   curl -X POST http://localhost:5000/api/stream/start \
   -H "Content-Type: application/json" \
   -d '{"rtsp_url": "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov"}'
   ```

### **Browser Console Errors:**

Press F12 in browser and check Console tab for errors:
- **CORS errors:** Backend not running
- **Network errors:** Wrong URL or backend down
- **404 errors:** Backend routes not working

### **Success Indicators:**

✅ Backend shows: `Stream started successfully`
✅ Frontend shows video loading
✅ No errors in browser console
✅ Overlays appear on video

### **Still Not Working?**

Try this simplified test:
1. Start only backend: `python app.py`
2. Open: http://localhost:5000/api/stream/video
3. Should show "Stream not started" or video feed

**Need Help?** Check the logs in terminal where you started the backend server.