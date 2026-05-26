import { useState } from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const Forecast = () => {
  const [loading, setLoading] = useState(false);
  const [showChart, setShowChart] = useState(false);

  // Simulation handler function logic
  const handleRunModel = () => {
    setLoading(true);
    setShowChart(false);

    setTimeout(() => {
      setLoading(false);
      setShowChart(true);
    }, 2000);
  };

  const chartData = {
    labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'],
    datasets: [
      {
        label: 'Predicted Demand (Linear Regression)',
        data: [440, 490, 510, 580, 620, 700],
        borderColor: 'rgb(37, 99, 235)',
        backgroundColor: 'rgba(37, 99, 235, 0.2)',
        tension: 0.3,
        fill: true,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'AI Model Demand Forecasting Output Values' },
    },
  };

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">AI Demand Forecasting</h1>
      
      <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 mb-6 max-w-md">
        <p className="text-gray-500 mb-4">
          Execute the trained Linear Regression matrix over the uploaded datasets to compute upcoming stock pipeline demands.
        </p>
        <button
          onClick={handleRunModel}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-5 py-2.5 rounded-lg transition disabled:bg-blue-300 cursor-pointer"
        >
          {loading ? 'Processing ML Model...' : 'Run Linear Regression Model'}
        </button>
      </div>

      {/* Loading Spinner Layout Layer */}
      {loading && (
        <div className="flex items-center gap-3 p-4 text-blue-600 font-medium">
          <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-600"></div>
          Analyzing data points and generating graphs...
        </div>
      )}

      {/* Dynamic Graph Chart View */}
      {showChart && (
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 max-w-3xl animate-fadeIn">
          <h2 className="text-lg font-bold text-gray-800 mb-4">Forecast Results Pipeline</h2>
          <Line data={chartData} options={chartOptions} />
        </div>
      )}
    </div>
  );
};

export default Forecast;