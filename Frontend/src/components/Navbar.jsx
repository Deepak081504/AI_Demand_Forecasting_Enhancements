import { Bell, User } from 'lucide-react';

const Navbar = () => {
  return (
    <header className="bg-white shadow p-4 flex justify-between items-center">
      <h2 className="text-xl font-semibold text-gray-700">Platform Overview</h2>
      <div className="flex items-center gap-4">
        <button className="text-gray-500 hover:text-blue-600"><Bell size={20} /></button>
        <div className="bg-gray-200 p-2 rounded-full text-gray-600"><User size={20} /></div>
      </div>
    </header>
  );
};
export default Navbar;