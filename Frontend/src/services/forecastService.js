import api from './api';

export const generateForecast = async () => {
  const response = await api.get('/forecast/generate');
  return response.data;
};