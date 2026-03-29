import React, { useState } from 'react';
import InsightCard from './components/InsightCard';

function App() {
  const [topic, setTopic] = useState('');
  const [newsFeed, setNewsFeed] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!topic) return;

    setLoading(true);
    try {
        const response = await fetch('http://localhost:8000/api/generate-feed', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: topic }),
        });
        const data = await response.json();
        setNewsFeed(data.data);
    } catch (err) {
        console.error("Failed to fetch", err);
    } finally {
        setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8 font-sans">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-3xl font-bold text-center text-blue-900 mb-8">
          MyET: AI-Native News Experience
        </h1>
        
        <form onSubmit={handleSearch} className="mb-8 flex gap-2">
          <input
            type="text"
            className="flex-1 p-4 rounded-lg border shadow-sm"
            placeholder="Enter a business or tech topic..."
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          />
          <button 
            type="submit"
            disabled={loading}
            className="bg-blue-600 text-white px-6 py-4 rounded-lg font-semibold hover:bg-blue-700"
          >
            {loading ? 'Processing...' : 'Generate Insights'}
          </button>
        </form>

        <div className="space-y-6">
          {newsFeed?.map((article, index) => (
            <InsightCard key={index} article={article} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;