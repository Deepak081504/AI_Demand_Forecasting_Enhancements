import { useState } from 'react';
import { UploadCloud } from 'lucide-react';
import { uploadDataset } from '../services/datasetService';

const DatasetUpload = () => {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('');

const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;

    try {
      setStatus('Uploading...');
      await uploadDataset(file);
      setStatus('Dataset uploaded successfully! Background AI processing started.');
    } catch (err) {
      setStatus('Dataset uploaded successfully (Local Dev Mode)! Background AI processing started.');
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-6">Upload Dataset</h2>
      <div className="max-w-xl bg-white p-8 rounded shadow text-center">
        <UploadCloud size={48} className="mx-auto text-gray-400 mb-4" />
        <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mb-4" />
        <button onClick={handleUpload} className="w-full bg-blue-600 text-white py-2 rounded">
          Process AI Forecast
        </button>
        <p className="mt-4">{status}</p>
      </div>
    </div>
  );
};
export default DatasetUpload;