import api from './api';

export const uploadDataset = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await api.post('/dataset/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data;
};

export const getAllDatasets = async () => {
  const response = await api.get('/dataset/list');
  return response.data;
};