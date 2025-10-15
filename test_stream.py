#!/usr/bin/env python3
"""
Quick test script to verify RTSP streaming works
"""
import cv2
import sys

def test_rtsp_url(url):
    print(f"Testing RTSP URL: {url}")
    
    try:
        cap = cv2.VideoCapture(url)
        
        if not cap.isOpened():
            print("❌ Failed to open RTSP stream")
            return False
        
        ret, frame = cap.read()
        if not ret or frame is None:
            print("❌ Failed to read frame from stream")
            cap.release()
            return False
        
        print(f"✅ Successfully connected! Frame size: {frame.shape}")
        cap.release()
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    # Test URLs
    test_urls = [
        "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov",
        "rtsp://rtsp.stream/pattern"
    ]
    
    print("🔍 Testing RTSP URLs...\n")
    
    for url in test_urls:
        success = test_rtsp_url(url)
        print("-" * 50)
        
    print("\n💡 If all tests fail, try:")
    print("1. Check internet connection")
    print("2. Try different RTSP URLs")
    print("3. Check if OpenCV is properly installed")