import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { BookOpen, Loader2, ArrowRight, CheckCircle } from 'lucide-react';
import { generateRoadmap } from '../services/api';

const RoadmapPage = ({ analysisData }) => {
  const navigate = useNavigate();
  const [roadmap, setRoadmap] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!analysisData) {
      navigate('/');
      return;
    }

    const fetchRoadmap = async () => {
      try {
        const payload = {
          target_role: analysisData.target_role,
          missing_skills: analysisData.missing_skills
        };
        const data = await generateRoadmap(payload);
        setRoadmap(data.roadmap);
      } catch (err) {
        console.error(err);
        setError("Failed to generate roadmap.");
      } finally {
        setIsLoading(false);
      }
    };

    fetchRoadmap();
  }, [analysisData, navigate]);

  if (!analysisData) return null;

  return (
    <div className="space-y-8 max-w-4xl mx-auto">
      <div className="text-center mb-12">
        <h1 className="text-3xl md:text-4xl font-bold text-slate-100 mb-4">Your Personalized Roadmap</h1>
        <p className="text-slate-400">Step-by-step guide to master the missing skills for {analysisData.target_role}</p>
      </div>

      {isLoading ? (
        <div className="flex flex-col items-center justify-center py-20 space-y-4">
          <Loader2 className="w-10 h-10 animate-spin text-primary" />
          <p className="text-slate-400">AI is crafting your roadmap...</p>
        </div>
      ) : error ? (
        <div className="p-6 bg-red-500/10 border border-red-500/20 rounded-xl text-center text-red-400">
          {error}
        </div>
      ) : (
        <div className="relative border-l-2 border-slate-700/50 ml-4 md:ml-0 md:pl-0 space-y-12">
          {roadmap && roadmap.map((step, index) => (
            <motion.div 
              key={index}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className="relative md:flex items-start md:space-x-8"
            >
              {/* Timeline dot */}
              <div className="absolute -left-[25px] md:relative md:left-0 w-12 h-12 rounded-full bg-surface border-4 border-background flex items-center justify-center z-10 shadow-lg">
                <span className="text-primary font-bold">{index + 1}</span>
              </div>

              <div className="glass-panel p-6 md:p-8 rounded-3xl flex-1 ml-6 md:ml-0 mt-2 md:mt-0 relative overflow-hidden group hover:border-primary/50 transition-colors">
                <div className="absolute top-0 right-0 p-6 opacity-5 group-hover:opacity-10 transition-opacity">
                  <BookOpen className="w-24 h-24 text-primary" />
                </div>
                
                <h3 className="text-xl font-bold text-slate-100 mb-2">{step.step_title}</h3>
                <p className="text-slate-400 mb-6 leading-relaxed">{step.description}</p>
                
                <div className="space-y-4">
                  <h4 className="text-sm font-semibold text-slate-300 uppercase tracking-wider">Recommended Resources</h4>
                  <ul className="space-y-2">
                    {step.resources.map((res, i) => (
                      <li key={i} className="flex items-start space-x-3 text-slate-300 bg-surface/50 p-3 rounded-xl border border-slate-700/30">
                        <ArrowRight className="w-4 h-4 text-secondary mt-0.5 flex-shrink-0" />
                        <span>{res}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </motion.div>
          ))}
          
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: roadmap?.length * 0.1 }}
            className="relative flex items-center justify-center pt-8"
          >
            <div className="glass-panel px-8 py-4 rounded-full flex items-center space-x-3 border-emerald-500/30 text-emerald-400">
              <CheckCircle className="w-5 h-5" />
              <span className="font-semibold">Ready for the role!</span>
            </div>
          </motion.div>
        </div>
      )}
    </div>
  );
};

export default RoadmapPage;
