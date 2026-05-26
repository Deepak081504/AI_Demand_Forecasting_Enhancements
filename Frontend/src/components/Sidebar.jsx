import { Link } from 'react-router-dom';
import { LayoutDashboard, TrendingUp, UploadCloud, FileText } from 'lucide-react';

const Sidebar = () => {
  return (
    <div className="w-64 bg-gray-900 text-white h-full p-4">
      <h2 className="text-2xl font-bold mb-8 text-center text-blue-400">AI Forecast</h2>
      <nav className="flex flex-col gap-4">
        <Link to="/dashboard" className="flex items-center gap-3 p-3 hover:bg-gray-800 rounded transition"><LayoutDashboard size={20}/> Dashboard</Link>
        <Link to="/forecast" className="flex items-center gap-3 p-3 hover:bg-gray-800 rounded transition"><TrendingUp size={20}/> Forecast</Link>
        <Link to="/dataset" className="flex items-center gap-3 p-3 hover:bg-gray-800 rounded transition"><UploadCloud size={20}/> Upload Data</Link>
        <Link to="/reports" className="flex items-center gap-3 p-3 hover:bg-gray-800 rounded transition"><FileText size={20}/> Reports</Link>
      </nav>
    </div>
  );
};

export default Sidebar;