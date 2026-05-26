import { FileSpreadsheet, FileText } from "lucide-react";

const Reports = () => {

  // 1. Excel Download Handler
  const handleDownloadExcel = () => {
    const csvContent = "data:text/csv;charset=utf-8," 
      + "Metric,Value\n"
      + "Total Users,12\n"
      + "Datasets Uploaded,5\n"
      + "Forecasting Accuracy,91%\n";

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "AI_Demand_Forecast_Report.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  // 2. PDF Download Handler
  const handleDownloadPDF = () => {
    const link = document.createElement("a");
    const dummyPdfContent = new Blob(["AI Demand Forecasting Platform - Summary Analytics Report Generated."], { type: 'application/pdf' });
    link.href = URL.createObjectURL(dummyPdfContent);
    link.setAttribute("download", "AI_Forecasting_Analytics.pdf");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">Export Analytics Reports</h1>
      
      <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 max-w-2xl">
        <p className="text-gray-500 mb-6">
          Select your preferred file format to download the latest AI demand forecasting model metrics and system activity logs.
        </p>

        <div className="flex flex-col sm:flex-row gap-4">
          {/* Excel Button */}
          <button 
            onClick={handleDownloadExcel}
            className="flex items-center justify-center gap-2 bg-green-600 hover:bg-green-700 text-white font-semibold px-6 py-3 rounded-lg shadow-sm transition-all duration-200 cursor-pointer"
          >
            <FileSpreadsheet size={20} />
            Download Excel Report
          </button>

          {/* PDF Button */}
          <button 
            onClick={handleDownloadPDF}
            className="flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 rounded-lg shadow-sm transition-all duration-200 cursor-pointer"
          >
            <FileText size={20} />
            Download PDF Report
          </button>
        </div>
      </div>
    </div>
  );
};

export default Reports;