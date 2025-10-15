import React, { useState, useEffect } from 'react';
import { overlayAPI } from '../services/api';

const OverlayManager = ({ onOverlaysChange }) => {
  const [overlays, setOverlays] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [editingOverlay, setEditingOverlay] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    type: 'text',
    content: '',
    position: { x: 10, y: 10 },
    size: { width: 200, height: 50 }
  });

  useEffect(() => {
    fetchOverlays();
  }, []);

  const fetchOverlays = async () => {
    try {
      const response = await overlayAPI.getAll();
      setOverlays(response.data);
      onOverlaysChange(response.data);
    } catch (error) {
      console.error('Error fetching overlays:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingOverlay) {
        await overlayAPI.update(editingOverlay._id, formData);
      } else {
        await overlayAPI.create(formData);
      }
      fetchOverlays();
      resetForm();
    } catch (error) {
      console.error('Error saving overlay:', error);
      alert('Failed to save overlay');
    }
  };

  const handleEdit = (overlay) => {
    setEditingOverlay(overlay);
    setFormData(overlay);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this overlay?')) {
      try {
        await overlayAPI.delete(id);
        fetchOverlays();
      } catch (error) {
        console.error('Error deleting overlay:', error);
        alert('Failed to delete overlay');
      }
    }
  };

  const resetForm = () => {
    setFormData({
      name: '',
      type: 'text',
      content: '',
      position: { x: 10, y: 10 },
      size: { width: 200, height: 50 }
    });
    setEditingOverlay(null);
    setShowForm(false);
  };

  return (
    <div>
      <button onClick={() => setShowForm(!showForm)} className="btn btn-add">
        {showForm ? '❌ Cancel' : '➕ Add New Overlay'}
      </button>

      {showForm && (
        <form onSubmit={handleSubmit} className="overlay-form">
          <h4 style={{ marginBottom: '20px', color: '#2d3748' }}>
            {editingOverlay ? '✏️ Edit Overlay' : '✨ Create New Overlay'}
          </h4>
          
          <div className="form-group">
            <label className="form-label">Name</label>
            <input
              type="text"
              value={formData.name}
              onChange={(e) => setFormData({...formData, name: e.target.value})}
              className="form-input"
              placeholder="Enter overlay name"
              required
            />
          </div>

          <div className="form-group">
            <label className="form-label">Type</label>
            <select
              value={formData.type}
              onChange={(e) => setFormData({...formData, type: e.target.value})}
              className="form-select"
            >
              <option value="text">📝 Text Overlay</option>
              <option value="image">🖼️ Image Overlay</option>
            </select>
          </div>

          <div className="form-group">
            <label className="form-label">Content</label>
            <input
              type="text"
              value={formData.content}
              onChange={(e) => setFormData({...formData, content: e.target.value})}
              className="form-input"
              placeholder={formData.type === 'text' ? 'Enter text content' : 'Enter image URL'}
              required
            />
          </div>

          <div className="form-group">
            <label className="form-label">Position</label>
            <div className="form-row">
              <input
                type="number"
                value={formData.position.x}
                onChange={(e) => setFormData({
                  ...formData, 
                  position: {...formData.position, x: parseInt(e.target.value) || 0}
                })}
                className="form-input"
                placeholder="X position"
              />
              <input
                type="number"
                value={formData.position.y}
                onChange={(e) => setFormData({
                  ...formData, 
                  position: {...formData.position, y: parseInt(e.target.value) || 0}
                })}
                className="form-input"
                placeholder="Y position"
              />
            </div>
          </div>

          <div className="form-group">
            <label className="form-label">Size</label>
            <div className="form-row">
              <input
                type="number"
                value={formData.size.width}
                onChange={(e) => setFormData({
                  ...formData, 
                  size: {...formData.size, width: parseInt(e.target.value) || 0}
                })}
                className="form-input"
                placeholder="Width"
              />
              <input
                type="number"
                value={formData.size.height}
                onChange={(e) => setFormData({
                  ...formData, 
                  size: {...formData.size, height: parseInt(e.target.value) || 0}
                })}
                className="form-input"
                placeholder="Height"
              />
            </div>
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <button type="submit" className="btn btn-primary">
              {editingOverlay ? '✅ Update' : '✨ Create'}
            </button>
            <button type="button" onClick={resetForm} className="btn btn-secondary">
              ❌ Cancel
            </button>
          </div>
        </form>
      )}

      <div style={{ marginTop: '25px' }}>
        <h4 style={{ color: '#2d3748', marginBottom: '15px' }}>Existing Overlays</h4>
        {overlays.length === 0 ? (
          <div style={{ 
            textAlign: 'center', 
            padding: '40px', 
            color: '#718096',
            background: '#f7fafc',
            borderRadius: '12px',
            border: '2px dashed #e2e8f0'
          }}>
            🎨 No overlays created yet.
            <br />
            <small>Click "Add New Overlay" to get started!</small>
          </div>
        ) : (
          <ul className="overlay-list">
            {overlays.map((overlay) => (
              <li key={overlay._id} className="overlay-item">
                <div className="overlay-name">
                  {overlay.type === 'text' ? '📝' : '🖼️'} {overlay.name}
                </div>
                <div className="overlay-details">
                  <strong>Type:</strong> {overlay.type === 'text' ? 'Text' : 'Image'}<br />
                  <strong>Content:</strong> {overlay.content.length > 50 ? overlay.content.substring(0, 50) + '...' : overlay.content}<br />
                  <strong>Position:</strong> ({overlay.position.x}, {overlay.position.y})<br />
                  <strong>Size:</strong> {overlay.size.width} × {overlay.size.height}px
                </div>
                <div className="overlay-actions">
                  <button onClick={() => handleEdit(overlay)} className="btn btn-edit">
                    ✏️ Edit
                  </button>
                  <button onClick={() => handleDelete(overlay._id)} className="btn btn-delete">
                    🗑️ Delete
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default OverlayManager;