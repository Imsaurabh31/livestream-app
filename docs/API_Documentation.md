# Livestream App API Documentation

## Base URL
```
http://localhost:5000/api
```

## Overlay Management Endpoints

### 1. Create Overlay
**POST** `/overlays`

Creates a new overlay configuration.

**Request Body:**
```json
{
  "name": "Logo Overlay",
  "type": "image",
  "content": "https://example.com/logo.png",
  "position": {
    "x": 10,
    "y": 10
  },
  "size": {
    "width": 100,
    "height": 50
  }
}
```

**Response:**
```json
{
  "id": "64f8a1b2c3d4e5f6a7b8c9d0",
  "message": "Overlay created successfully"
}
```

### 2. Get All Overlays
**GET** `/overlays`

Retrieves all overlay configurations.

**Response:**
```json
[
  {
    "_id": "64f8a1b2c3d4e5f6a7b8c9d0",
    "name": "Logo Overlay",
    "type": "image",
    "content": "https://example.com/logo.png",
    "position": {
      "x": 10,
      "y": 10
    },
    "size": {
      "width": 100,
      "height": 50
    },
    "created_at": "2023-09-06T10:30:00Z",
    "updated_at": "2023-09-06T10:30:00Z"
  }
]
```

### 3. Get Overlay by ID
**GET** `/overlays/{id}`

Retrieves a specific overlay by its ID.

**Response:**
```json
{
  "_id": "64f8a1b2c3d4e5f6a7b8c9d0",
  "name": "Logo Overlay",
  "type": "image",
  "content": "https://example.com/logo.png",
  "position": {
    "x": 10,
    "y": 10
  },
  "size": {
    "width": 100,
    "height": 50
  },
  "created_at": "2023-09-06T10:30:00Z",
  "updated_at": "2023-09-06T10:30:00Z"
}
```

### 4. Update Overlay
**PUT** `/overlays/{id}`

Updates an existing overlay configuration.

**Request Body:**
```json
{
  "name": "Updated Logo",
  "position": {
    "x": 20,
    "y": 20
  }
}
```

**Response:**
```json
{
  "message": "Overlay updated successfully"
}
```

### 5. Delete Overlay
**DELETE** `/overlays/{id}`

Deletes an overlay configuration.

**Response:**
```json
{
  "message": "Overlay deleted successfully"
}
```

## Stream Management Endpoints

### 1. Start Stream
**POST** `/stream/start`

Starts streaming from an RTSP URL.

**Request Body:**
```json
{
  "rtsp_url": "rtsp://example.com/stream"
}
```

**Response:**
```json
{
  "message": "Stream started successfully"
}
```

### 2. Stop Stream
**POST** `/stream/stop`

Stops the current stream.

**Response:**
```json
{
  "message": "Stream stopped successfully"
}
```

### 3. Get Stream Status
**GET** `/stream/status`

Gets the current streaming status.

**Response:**
```json
{
  "streaming": true,
  "rtsp_url": "rtsp://example.com/stream"
}
```

### 4. Video Feed
**GET** `/stream/video`

Returns the live video feed as a multipart stream.

**Response:** Multipart HTTP stream with JPEG frames

## Error Responses

All endpoints may return the following error responses:

**400 Bad Request:**
```json
{
  "error": "Missing required fields"
}
```

**404 Not Found:**
```json
{
  "error": "Overlay not found"
}
```

**500 Internal Server Error:**
```json
{
  "error": "Internal server error"
}
```

## Data Models

### Overlay Model
```json
{
  "_id": "string",
  "name": "string",
  "type": "text|image",
  "content": "string",
  "position": {
    "x": "number",
    "y": "number"
  },
  "size": {
    "width": "number",
    "height": "number"
  },
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Field Descriptions

- **name**: Display name for the overlay
- **type**: Either "text" for text overlays or "image" for image overlays
- **content**: For text overlays, this is the text content. For image overlays, this is the image URL
- **position**: X and Y coordinates for overlay placement (in pixels)
- **size**: Width and height of the overlay (in pixels)
- **created_at**: Timestamp when the overlay was created
- **updated_at**: Timestamp when the overlay was last updated