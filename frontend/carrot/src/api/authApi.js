import axios from 'axios';

const BASE_URL = 'http://localhost:8006/api/';

const authApi = axios.create({
  baseURL: BASE_URL,
  withCredentials: true,
});

authApi.defaults.headers.common['Content-Type'] = 'application/json';

export const getAccessTokenFn = async (user) => {
  const response = await authApi.post('auth/token', user);
  return response.data;
};

export const refreshAccessTokenFn = async () => {
  const response = await authApi.get('auth/token/refresh');
  return response.data;
};

export const getCurrentUserFn = async () => {
  const response = await authApi.get('users/me/');
  return response.data;
};

authApi.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    const code = error.response.data.code;
    if (code === 'token_not_valid' && !originalRequest._retry) {
      originalRequest._retry = true;
      await refreshAccessTokenFn();
      return authApi(originalRequest);
    }
    return Promise.reject(error);
  }
);