import React from 'react';

const InsightCard = ({ article }) => {
  return (
    <div className="bg-white rounded-xl shadow-md p-6 border border-gray-100">
      <h2 className="text-xl font-bold text-gray-800 mb-3">{article.headline}</h2>
      
      <div className="mb-4">
        <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-1">AI Summary</h3>
        <p className="text-gray-700 leading-relaxed">{article.summary}</p>
      </div>

      <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded-r-md">
        <h3 className="text-sm font-semibold text-blue-800 uppercase tracking-wider mb-1">Why This Matters To You</h3>
        <p className="text-blue-900">{article.contextual_insight}</p>
      </div>
      
      <button className="mt-4 text-blue-600 font-medium text-sm hover:underline">
        Ask a follow-up question
      </button>
    </div>
  );
};

export default InsightCard;