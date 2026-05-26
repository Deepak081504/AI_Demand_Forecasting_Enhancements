import { useEffect, useState } from "react";
import api from "../services/api"; 
import AnalyticsChart from "../components/AnalyticsChart";
import { Activity, Users, Database, TrendingUp } from "lucide-react";

const Dashboard = () => {
  const [stats, setStats] = useState({
    users: 0,
    datasets: 0,
    forecasts: 0,
    notifications: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboardStats = async () => {
      try {
        const response = await api.get("/dashboard/stats"); 
        setStats(response.data);
      } catch (error) {
        console.log("Backend offline or connection error. Showing default dev data.");
      
        setStats({
          users: 12,
          datasets: 5,
          forecasts: 24,
          notifications: 3,
        });
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardStats();
  }, []);

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">Admin Dashboard</h1>

      {/* Grid Layout for Analytics Metrics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        {/* Users Card */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center justify-between">
          <div>
            <p className="text-gray-400 text-sm font-medium uppercase">Users</p>
            <h3 className="text-3xl font-bold text-gray-800">{stats.users}</h3>
          </div>
          <div className="bg-blue-50 p-3 rounded-lg text-blue-600"><Users size={24} /></div>
        </div>

        {/* Datasets Card */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center justify-between">
          <div>
            <p className="text-gray-400 text-sm font-medium uppercase">Datasets</p>
            <h3 className="text-3xl font-bold text-gray-800">{stats.datasets}</h3>
          </div>
          <div className="bg-green-50 p-3 rounded-lg text-green-600"><Database size={24} /></div>
        </div>

        {/* Forecasts Card */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center justify-between">
          <div>
            <p className="text-gray-400 text-sm font-medium uppercase">Forecasts</p>
            <h3 className="text-3xl font-bold text-gray-800">{stats.forecasts}</h3>
          </div>
          <div className="bg-purple-50 p-3 rounded-lg text-purple-600"><TrendingUp size={24} /></div>
        </div>

        {/* Notifications Card */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center justify-between">
          <div>
            <p className="text-gray-400 text-sm font-medium uppercase">Notifications</p>
            <h3 className="text-3xl font-bold text-gray-800">{stats.notifications}</h3>
          </div>
          <div className="bg-red-50 p-3 rounded-lg text-red-600"><Activity size={24} /></div>
        </div>
      </div>

      {/* System activity charts layers */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 min-h-[300px]">
          <h2 className="text-lg font-bold text-gray-800 mb-4">System Activity</h2>
          <div className="text-gray-400 text-center mt-12">Live operations logs waiting for streaming...</div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
          <h2 className="text-lg font-bold text-gray-800 mb-4">Forecasting Accuracy</h2>
          <AnalyticsChart />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;