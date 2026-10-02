import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import UploadPage from './pages/UploadPage';
import DashboardPage from './pages/DashboardPage';
import RoadmapPage from './pages/RoadmapPage';
import { useState } from 'react';

function App() {
  const [analysisData, setAnalysisData] = useState(null);

  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<UploadPage setAnalysisData={setAnalysisData} />} />
          <Route path="/dashboard" element={<DashboardPage analysisData={analysisData} />} />
          <Route path="/roadmap" element={<RoadmapPage analysisData={analysisData} />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
