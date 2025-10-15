import React, { useState } from 'react';
import VideoPlayer from './components/VideoPlayer';
import OverlayManager from './components/OverlayManager';
import './App.css';

function App() {
  const [overlays, setOverlays] = useState([]);

  const handleOverlaysChange = (newOverlays) => {
    setOverlays(newOverlays);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Livestream App</h1>
        <p>Stream RTSP videos with custom overlays</p>
      </header>

      <main>
        <div className="main-grid">
          <div className="video-section">
            <h2>Video Player</h2>
            <VideoPlayer overlays={overlays} />
          </div>
          
          <div className="overlay-section">
            <h2>Overlay Manager</h2>
            <OverlayManager onOverlaysChange={handleOverlaysChange} />
          </div>
        </div>

        <div className="instructions">
          <h3>How to Use</h3>
          <ol>
            <li>Enter an RTSP URL in the video player (you can use RTSP.me or similar services for testing)</li>
            <li>Click "Play" to start the livestream</li>
            <li>Use the Overlay Manager to create text or image overlays</li>
            <li>Overlays will appear on top of the video stream</li>
            <li>You can edit or delete overlays as needed</li>
          </ol>
          
          <div className="sample-urls">
            <h4>Sample RTSP URLs for Testing:</h4>
            <ul>
              <li>rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov</li>
              <li>rtsp://rtsp.stream/pattern</li>
            </ul>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;