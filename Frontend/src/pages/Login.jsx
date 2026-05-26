import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { login } from '../services/authService';
import { useAuth } from '../hooks/useAuth';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { setUser } = useAuth(); 

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(''); 
    
    const savedUserRaw = localStorage.getItem('registeredUser');
    
    if (!savedUserRaw) {
      setError('No user registered yet! Please sign up first.');
      return;
    }

    const savedUser = JSON.parse(savedUserRaw);

    if (email === savedUser.email && password === savedUser.password) {
      setUser({ email: savedUser.email, name: savedUser.name });
      navigate('/dashboard');
    } else {
      setError('Invalid Email or Password! Try again.');
    }
  };
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh', backgroundColor: '#f3f4f6', fontFamily: 'sans-serif' }}>
      <div style={{ backgroundColor: '#ffffff', padding: '2.5rem', borderRadius: '0.5rem', boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1)', width: '24rem' }}>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', textAlign: 'center', marginBottom: '1.5rem', color: '#2563eb' }}>
          AI Demand Forecasting Login
        </h2>
        
        {error && <p style={{ color: '#ef4444', fontSize: '0.875rem', marginBottom: '1rem', textAlign: 'center' }}>{error}</p>}
        
        <form onSubmit={handleLogin}>
          <div style={{ marginBottom: '1rem' }}>
            <label style={{ display: 'block', color: '#374151', fontWeight: '500', marginBottom: '0.5rem' }}>Email Address</label>
            <input 
              type="email" 
              style={{ width: '100%', border: '1px solid #d1d5db', padding: '0.5rem', borderRadius: '0.375rem', boxSizing: 'border-box' }}
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
              placeholder=""
              required 
            />
          </div>
          
          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{ display: 'block', color: '#374151', fontWeight: '500', marginBottom: '0.5rem' }}>Password</label>
            <input 
              type="password" 
              style={{ width: '100%', border: '1px solid #d1d5db', padding: '0.5rem', borderRadius: '0.375rem', boxSizing: 'border-box' }}
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
              placeholder=""
              required 
            />
          </div>
          
          <button 
            type="submit" 
            style={{ width: '100%', backgroundColor: '#2563eb', color: '#ffffff', fontWeight: 'bold', padding: '0.75rem', borderRadius: '0.375rem', border: 'none', cursor: 'pointer' }}
          >
            Sign In to Platform
          </button>
        </form>
        <p style={{ textAlign: 'center', fontSize: '0.875rem', color: '#6b7280', marginTop: '1rem' }}>
          Don't have an account?{' '}
          <span onClick={() => navigate('/register')} style={{ color: '#10b981', cursor: 'pointer', fontWeight: '500' }}>
            Register here
          </span>
        </p>
      </div>
    </div>
  );
};

export default Login;