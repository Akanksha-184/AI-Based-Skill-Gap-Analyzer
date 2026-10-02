import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { CheckCircle2, XCircle, TrendingUp, ArrowRight } from 'lucide-react';

const DashboardPage = ({ analysisData }) => {
  const navigate = useNavigate();

  useEffect(() => {
    if (!analysisData) {
      navigate('/');
    }
  }, [analysisData, navigate]);

  if (!analysisData) return null;

  const { target_role, match_score, present_skills, missing_skills } = analysisData;
  const scoreValue = parseFloat(match_score.replace('%', ''));

  // Animation variants
  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: { staggerChildren: 0.1 }
    }
  };

  const item = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0 }
  };

  return (
    <div className="space-y-8">
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-slate-100">Gap Analysis</h1>
          <p className="text-slate-400 mt-1">Target Role: <span className="text-primary font-medium">{target_role}</span></p>
        </div>
        <button
          onClick={() => navigate('/roadmap')}
          className="flex items-center space-x-2 px-6 py-3 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl text-white font-medium transition-colors"
        >
          <span>View Learning Roadmap</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Score Card */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className="lg:col-span-1 glass-panel rounded-3xl p-8 flex flex-col items-center justify-center text-center relative overflow-hidden"
        >
          <div className="absolute top-0 right-0 p-6 opacity-10">
            <TrendingUp className="w-32 h-32" />
          </div>
          
          <h3 className="text-lg font-medium text-slate-300 mb-6 relative z-10">Match Score</h3>
          
          <div className="relative w-48 h-48 flex items-center justify-center z-10">
            <svg className="w-full h-full transform -rotate-90">
              <circle
                cx="96"
                cy="96"
                r="88"
                className="stroke-slate-800"
                strokeWidth="12"
                fill="none"
              />
              <motion.circle
                initial={{ strokeDashoffset: 2 * Math.PI * 88 }}
                animate={{ strokeDashoffset: 2 * Math.PI * 88 * (1 - scoreValue / 100) }}
                transition={{ duration: 1.5, ease: "easeOut" }}
                cx="96"
                cy="96"
                r="88"
                className="stroke-primary"
                strokeWidth="12"
                fill="none"
                strokeDasharray={2 * Math.PI * 88}
                strokeLinecap="round"
              />
            </svg>
            <div className="absolute flex flex-col items-center">
              <span className="text-5xl font-bold text-white">{match_score}</span>
            </div>
          </div>
          
          <p className="mt-6 text-slate-400 text-sm relative z-10">
            {scoreValue >= 80 ? "Excellent match! You're nearly there." :
             scoreValue >= 50 ? "Good foundation. A few key skills missing." :
             "Significant skill gap. Focus on the core requirements."}
          </p>
        </motion.div>

        {/* Skills Lists */}
        <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Present Skills */}
          <motion.div 
            variants={container}
            initial="hidden"
            animate="show"
            className="glass-panel rounded-3xl p-6"
          >
            <div className="flex items-center space-x-3 mb-6">
              <div className="p-2 bg-emerald-500/20 rounded-lg">
                <CheckCircle2 className="w-5 h-5 text-emerald-400" />
              </div>
              <h3 className="text-lg font-medium text-slate-200">Skills You Have</h3>
            </div>
            
            {present_skills.length > 0 ? (
              <div className="flex flex-wrap gap-2">
                {present_skills.map((skill, i) => (
                  <motion.span
                    key={i}
                    variants={item}
                    className="px-3 py-1.5 bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 rounded-lg text-sm"
                  >
                    {skill}
                  </motion.span>
                ))}
              </div>
            ) : (
              <p className="text-slate-500 text-sm">No matching skills found in the resume.</p>
            )}
          </motion.div>

          {/* Missing Skills */}
          <motion.div 
            variants={container}
            initial="hidden"
            animate="show"
            className="glass-panel rounded-3xl p-6"
          >
            <div className="flex items-center space-x-3 mb-6">
              <div className="p-2 bg-red-500/20 rounded-lg">
                <XCircle className="w-5 h-5 text-red-400" />
              </div>
              <h3 className="text-lg font-medium text-slate-200">Skills to Learn</h3>
            </div>
            
            {missing_skills.length > 0 ? (
              <div className="flex flex-wrap gap-2">
                {missing_skills.map((skill, i) => (
                  <motion.span
                    key={i}
                    variants={item}
                    className="px-3 py-1.5 bg-red-500/10 border border-red-500/20 text-red-300 rounded-lg text-sm"
                  >
                    {skill}
                  </motion.span>
                ))}
              </div>
            ) : (
              <p className="text-slate-500 text-sm">You have all the required core skills!</p>
            )}
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
