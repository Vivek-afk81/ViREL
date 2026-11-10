import { useEffect, useState } from 'react';
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import { checkHealth } from './services/api';

export default function App() {
  const [health, setHealth] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    checkHealth()
      .then((data) => setHealth(data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>WeeBies</h1>
      {health && (
        <p style={{ color: 'green' }}>
          Backend Status: <strong>{health.status}</strong> ({health.service})
        </p>
      )}
      {error && (
        <p style={{ color: 'red' }}>
          Backend connection error: {error}
        </p>
      )}
    </div>
  );
}