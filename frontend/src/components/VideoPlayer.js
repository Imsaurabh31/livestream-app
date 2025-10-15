import React, { useState, useRef, useEffect } from 'react';
import { streamAPI } from '../services/api';

const VideoPlayer = ({ overlays }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [rtspUrl, setRtspUrl] = useState('Demo Stream - Click Play');
  const [volume, setVolume] = useState(1);
  const [error, setError] = useState('');
  const videoRef = useRef(null);
  const imgRef = useRef(null);

  const handlePlay = async () => {
    setError('');
    try {
      await streamAPI.start(rtspUrl || 'demo');
      setIsPlaying(true);
      
      if (imgRef.current) {
        const baseUrl = process.env.NODE_ENV === 'production' ? '' : 'http://127.0.0.1:5000';
        imgRef.current.src = `${baseUrl}/api/stream/video?t=${Date.now()}`;
        imgRef.current.onload = () => setError('');
        imgRef.current.onerror = () => {
          setError('Backend not running. Start backend first.');
          setIsPlaying(false);
        };
      }
    } catch (error) {
      setError('Backend not running. Start backend first.');
      setIsPlaying(false);
    }
  };

  const handleStop = async () => {
    try {
      await streamAPI.stop();
      setIsPlaying(false);
      setError('');
      if (imgRef.current) {
        imgRef.current.src = '';
      }
    } catch (error) {
      console.error('Error stopping stream:', error);
    }
  };

  const handleVolumeChange = (e) => {
    const newVolume = parseFloat(e.target.value);
    setVolume(newVolume);
  };

  return (
    <div>
      <div className="url-input-container">
        <input
          type="text"
          placeholder="🎬 Enter RTSP URL (e.g., rtsp://example.com/stream)"
          value={rtspUrl}
          onChange={(e) => setRtspUrl(e.target.value)}
          className="url-input"
        />
        <button onClick={isPlaying ? handleStop : handlePlay} className="play-button">
          {isPlaying ? '⏹️ Stop' : '▶️ Play'}
        </button>
      </div>

      <div className="video-container">
        {error && (
          <div style={{
            position: 'absolute',
            top: '10px',
            left: '10px',
            right: '10px',
            background: 'rgba(239, 68, 68, 0.9)',
            color: 'white',
            padding: '10px',
            borderRadius: '8px',
            fontSize: '14px',
            zIndex: 10
          }}>
            ⚠️ {error}
          </div>
        )}
        
        {isPlaying ? (
          <img
            ref={imgRef}
            alt="Live Stream"
            className="video-stream"
            style={{ display: 'block' }}
          />
        ) : (
          <div className="video-placeholder">
            🎥 Click Play to start livestream
          </div>
        )}

        {/* Render overlays */}
        {overlays.map((overlay) => (
          <div
            key={overlay._id}
            style={{
              position: 'absolute',
              left: `${overlay.position.x}px`,
              top: `${overlay.position.y}px`,
              width: `${overlay.size.width}px`,
              height: `${overlay.size.height}px`,
              backgroundColor: overlay.type === 'text' ? 'rgba(0,0,0,0.8)' : 'transparent',
              color: 'white',
              padding: overlay.type === 'text' ? '8px 12px' : '0',
              fontSize: overlay.type === 'text' ? '16px' : 'inherit',
              fontWeight: overlay.type === 'text' ? '600' : 'normal',
              borderRadius: overlay.type === 'text' ? '8px' : '0',
              pointerEvents: 'none',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              textShadow: overlay.type === 'text' ? '0 2px 4px rgba(0,0,0,0.8)' : 'none',
            }}
          >
            {overlay.type === 'text' ? overlay.content : (
              <img 
                src={overlay.content} 
                alt="Overlay" 
                style={{ 
                  width: '100%', 
                  height: '100%', 
                  objectFit: 'contain',
                  borderRadius: '8px'
                }} 
              />
            )}
          </div>
        ))}
      </div>

      <div className="volume-control">
        <span>🔊</span>
        <input
          type="range"
          min="0"
          max="1"
          step="0.1"
          value={volume}
          onChange={handleVolumeChange}
          className="volume-slider"
        />
        <span style={{ fontWeight: '600', minWidth: '45px' }}>{Math.round(volume * 100)}%</span>
      </div>
    </div>
  );
};

export default VideoPlayer;