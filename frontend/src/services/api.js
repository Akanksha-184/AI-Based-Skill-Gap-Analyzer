import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const analyzeResume = async (formData) => {
  const response = await axios.post(`${API_BASE_URL}/analyze`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const generateRoadmap = async (data) => {
  const response = await api.post('/roadmap', data);
  return response.data;
};

export const chatWithAI = async (message) => {
  const response = await api.post('/chat', { message });
  return response.data;
};

export default api;
