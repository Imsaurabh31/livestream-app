import axios from 'axios';

const API_BASE_URL = 'https://livestream-app-git-main-mishrasaurabhstms-projects.vercel.app/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const overlayAPI = {
  create: (data) => api.post('/overlays', data),
  getAll: () => api.get('/overlays'),
  getById: (id) => api.get(`/overlays/${id}`),
  update: (id, data) => api.put(`/overlays/${id}`, data),
  delete: (id) => api.delete(`/overlays/${id}`),
};

export const streamAPI = {
  start: (rtspUrl) => api.post('/stream/start', { rtsp_url: rtspUrl }),
  stop: () => api.post('/stream/stop'),
  getStatus: () => api.get('/stream/status'),
};

export default api;