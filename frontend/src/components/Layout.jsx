import Navbar from './Navbar';
import Chatbot from './Chatbot';

const Layout = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-grow pt-20 pb-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        {children}
      </main>
      <Chatbot />
    </div>
  );
};

export default Layout;
