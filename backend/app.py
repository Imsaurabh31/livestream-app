from flask import Flask, jsonify
from flask_cors import CORS
from routes.overlay_routes import overlay_bp
from routes.stream_routes import stream_bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(overlay_bp, url_prefix='/api')
app.register_blueprint(stream_bp, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({
        'message': 'Livestream API Server',
        'version': '1.0.0',
        'endpoints': {
            'overlays': '/api/overlays',
            'stream': '/api/stream'
        }
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)