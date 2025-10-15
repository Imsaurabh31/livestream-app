from flask import Blueprint, request, jsonify
from models.overlay import Overlay

overlay_bp = Blueprint('overlay', __name__)
overlay_model = Overlay()

@overlay_bp.route('/overlays', methods=['POST'])
def create_overlay():
    try:
        data = request.get_json()
        required_fields = ['name', 'type', 'content', 'position', 'size']
        
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        overlay_id = overlay_model.create(data)
        return jsonify({'id': overlay_id, 'message': 'Overlay created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@overlay_bp.route('/overlays', methods=['GET'])
def get_overlays():
    try:
        overlays = overlay_model.get_all()
        return jsonify(overlays), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@overlay_bp.route('/overlays/<overlay_id>', methods=['GET'])
def get_overlay(overlay_id):
    try:
        overlay = overlay_model.get_by_id(overlay_id)
        if not overlay:
            return jsonify({'error': 'Overlay not found'}), 404
        return jsonify(overlay), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@overlay_bp.route('/overlays/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    try:
        data = request.get_json()
        success = overlay_model.update(overlay_id, data)
        if not success:
            return jsonify({'error': 'Overlay not found'}), 404
        return jsonify({'message': 'Overlay updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@overlay_bp.route('/overlays/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    try:
        success = overlay_model.delete(overlay_id)
        if not success:
            return jsonify({'error': 'Overlay not found'}), 404
        return jsonify({'message': 'Overlay deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500