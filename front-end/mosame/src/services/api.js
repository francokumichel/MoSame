import axios from "axios";

export const apiService = axios.create({
  baseURL: "/api",
  xsrfCookieName: "csrf_access_token",
});

// Esto garantiza que el token se lea del localStorage justo antes de cada envío
apiService.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});