import { Link, useLocation } from 'react-router-dom';
import { Target, BarChart2, Map } from 'lucide-react';
import { motion } from 'framer-motion';

const Navbar = () => {
  const location = useLocation();

  const navItems = [
    { name: 'Upload', path: '/', icon: Target },
    { name: 'Dashboard', path: '/dashboard', icon: BarChart2 },
    { name: 'Roadmap', path: '/roadmap', icon: Map },
  ];

  return (
    <nav className="fixed top-0 w-full z-50 glass-panel border-b border-slate-700/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-accent flex items-center justify-center">
              <Target className="w-5 h-5 text-white" />
            </div>
            <span className="font-bold text-xl text-gradient">GapAnalyzer</span>
          </div>
          
          <div className="hidden md:block">
            <div className="flex space-x-4">
              {navItems.map((item) => {
                const isActive = location.pathname === item.path;
                const Icon = item.icon;
                
                return (
                  <Link
                    key={item.name}
                    to={item.path}
                    className="relative px-3 py-2 rounded-md text-sm font-medium transition-colors"
                  >
                    <span className={`flex items-center space-x-1 ${isActive ? 'text-white' : 'text-slate-400 hover:text-white'}`}>
                      <Icon className="w-4 h-4" />
                      <span>{item.name}</span>
                    </span>
                    {isActive && (
                      <motion.div
                        layoutId="navbar-indicator"
                        className="absolute bottom-0 left-0 right-0 h-0.5 bg-primary rounded-t-full"
                        transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                      />
                    )}
                  </Link>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
