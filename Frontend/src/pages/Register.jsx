import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { register } from '../services/authService';

const Register = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

 const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const userData = { name, email, password };
      localStorage.setItem('registeredUser', JSON.stringify(userData));

      setSuccess('Registration successful! Redirecting to login...');
      setError('');
      setTimeout(() => navigate('/login'), 2000);
    } catch (err) {
      setError('Registration failed.');
    }
  };

  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh', backgroundColor: '#f3f4f6', fontFamily: 'sans-serif' }}>
      <div style={{ backgroundColor: '#ffffff', padding: '2.5rem', borderRadius: '0.5rem', boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1)', width: '24rem' }}>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', textAlign: 'center', marginBottom: '1.5rem', color: '#10b981' }}>
          Create Account
        </h2>
        
        {error && <p style={{ color: '#ef4444', fontSize: '0.875rem', marginBottom: '1rem', textAlign: 'center' }}>{error}</p>}
        {success && <p style={{ color: '#10b981', fontSize: '0.875rem', marginBottom: '1rem', textAlign: 'center' }}>{success}</p>}
        
        <form onSubmit={handleRegister}>
          <div style={{ marginBottom: '1rem' }}>
            <label style={{ display: 'block', color: '#374151', fontWeight: '500', marginBottom: '0.5rem' }}>Full Name</label>
            <input 
              type="text" 
              style={{ width: '100%', border: '1px solid #d1d5db', padding: '0.5rem', borderRadius: '0.375rem', boxSizing: 'border-box' }}
              value={name} 
              onChange={(e) => setName(e.target.value)} 
              placeholder=" "
              required 
            />
          </div>

          <div style={{ marginBottom: '1rem' }}>
            <label style={{ display: 'block', color: '#374151', fontWeight: '500', marginBottom: '0.5rem' }}>Email Address</label>
            <input 
              type="email" 
              style={{ width: '100%', border: '1px solid #d1d5db', padding: '0.5rem', borderRadius: '0.375rem', boxSizing: 'border-box' }}
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
              placeholder=" "
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
              placeholder=" "
              required 
            />
          </div>
          
          <button 
            type="submit" 
            style={{ width: '100%', backgroundColor: '#10b981', color: '#ffffff', fontWeight: 'bold', padding: '0.75rem', borderRadius: '0.375rem', border: 'none', cursor: 'pointer', marginBottom: '1rem' }}
          >
            Sign Up
          </button>
        </form>

        <p style={{ textAlign: 'center', fontSize: '0.875rem', color: '#6b7280' }}>
          Already have an account?{' '}
          <span onClick={() => navigate('/login')} style={{ color: '#2563eb', cursor: 'pointer', fontWeight: '500' }}>
            Login here
          </span>
        </p>
      </div>
    </div>
  );
};

export default Register;