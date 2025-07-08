import axios from 'axios';

// Base URL pointing to your Django backend
const API = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/', // Change to your deployed backend URL when live
  withCredentials: true,
});

// Request interceptor to add token to headers
API.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Token ${token}`; // DRF TokenAuth header
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Optional response interceptor for error handling/logging
API.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      console.warn('Unauthorized. Redirect to login or clear token.');
      // Optional: logout logic or redirect
    }
    return Promise.reject(error);
  }
);

export default API;
