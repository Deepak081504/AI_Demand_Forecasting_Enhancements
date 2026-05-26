import { Loader2 } from 'lucide-react';

const Loader = () => {
  return (
    <div className="flex justify-center items-center p-8">
      <Loader2 className="w-10 h-10 animate-spin text-blue-600" />
      <span className="ml-3 text-gray-600 font-medium">Processing...</span>
    </div>
  );
};

export default Loader;