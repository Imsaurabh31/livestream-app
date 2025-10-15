from flask import Flask, jsonify, Response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

streaming = False
rtsp_url = ""

@app.route('/')
def home():
    return jsonify({'message': 'Livestream API Server', 'status': 'running'})

@app.route('/api/stream/start', methods=['POST'])
def start_stream():
    global streaming, rtsp_url
    from flask import request
    data = request.get_json() or {}
    streaming = True
    rtsp_url = data.get('rtsp_url', 'demo_stream')
    return jsonify({'message': 'Stream started successfully'}), 200

@app.route('/api/stream/stop', methods=['POST'])
def stop_stream():
    global streaming
    streaming = False
    return jsonify({'message': 'Stream stopped successfully'}), 200

@app.route('/api/stream/video')
def video_feed():
    def generate():
        # Simple demo image as JPEG
        demo_frame = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xfe\x00\x13Created with GIMP\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\'" \x0c\x0c(7),01444\x1f\'9=82<.342\xff\xc0\x00\x11\x08\x01\x90\x02X\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00\x3f\x00\xf7\xfa(\xa2\x80\x0f\xff\xd9'
        
        while streaming:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + demo_frame + b'\r\n')
            time.sleep(0.1)
    
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Overlay routes
overlays = []

@app.route('/api/overlays', methods=['GET'])
def get_overlays():
    return jsonify(overlays)

@app.route('/api/overlays', methods=['POST'])
def create_overlay():
    from flask import request
    data = request.get_json()
    data['_id'] = str(len(overlays) + 1)
    overlays.append(data)
    return jsonify({'id': data['_id'], 'message': 'Overlay created'}), 201

@app.route('/api/overlays/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    from flask import request
    data = request.get_json()
    for i, overlay in enumerate(overlays):
        if overlay['_id'] == overlay_id:
            overlays[i].update(data)
            return jsonify({'message': 'Updated'})
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/overlays/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    global overlays
    overlays = [o for o in overlays if o['_id'] != overlay_id]
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__':
    print("Starting Livestream Backend...")
    print("Server running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)