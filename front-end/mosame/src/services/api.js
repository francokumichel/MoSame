import axios from "axios";

export const apiService = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  xsrfCookieName: "csrf_access_token",
  headers: {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  },
});