from flask import Blueprint, request, jsonify, Response
import requests
import time
import threading

stream_bp = Blueprint('stream', __name__)

class SimpleStreamer:
    def __init__(self):
        self.streaming = False
        self.rtsp_url = None
    
    def start_stream(self, rtsp_url):
        self.rtsp_url = rtsp_url
        self.streaming = True
        return True
    
    def stop_stream(self):
        self.streaming = False
    
    def generate_frames(self):
        # Simple demo frame generator
        import base64
        
        # Create a simple colored frame as demo
        demo_frame = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\'" \x0c\x0c(7),01444\x1f\'9=82<.342\xff\xc0\x00\x11\x08\x00\xc8\x01\x90\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00\x3f\x00\xf7\xfa(\xa2\x80\x0f\xff\xd9'
        
        while self.streaming:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + demo_frame + b'\r\n')
            time.sleep(0.1)

streamer = SimpleStreamer()

@stream_bp.route('/stream/start', methods=['POST'])
def start_stream():
    try:
        data = request.get_json()
        rtsp_url = data.get('rtsp_url')
        
        if not rtsp_url:
            return jsonify({'error': 'RTSP URL is required'}), 400
        
        # Basic RTSP URL validation
        if not rtsp_url.startswith(('rtsp://', 'http://', 'https://')):
            return jsonify({'error': 'Invalid URL format. Must start with rtsp://, http://, or https://'}), 400
        
        logger.info(f"Starting stream for URL: {rtsp_url}")
        success = streamer.start_stream(rtsp_url)
        
        if success:
            return jsonify({
                'message': 'Stream started successfully',
                'rtsp_url': rtsp_url,
                'stream_endpoint': '/api/stream/video'
            }), 200
        else:
            return jsonify({
                'error': 'Failed to connect to RTSP stream. Please check the URL and ensure the stream is accessible.'
            }), 500
            
    except Exception as e:
        logger.error(f"Error in start_stream: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@stream_bp.route('/stream/stop', methods=['POST'])
def stop_stream():
    try:
        streamer.stop_stream()
        return jsonify({'message': 'Stream stopped successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@stream_bp.route('/stream/video')
def video_feed():
    return Response(streamer.generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@stream_bp.route('/stream/status', methods=['GET'])
def stream_status():
    return jsonify({
        'streaming': streamer.streaming,
        'rtsp_url': streamer.rtsp_url
    }), 200