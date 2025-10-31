import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { BookProvider } from './context/BookContext';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';
import './App.css';

function App() {
  return (
    // 1. Sediakan Context di level tertinggi
    <BookProvider>
      {/* 2. Setup Router */}
      <BrowserRouter>
        <div className="app-container">
          <nav className="main-nav">
            <h1>Manajemen Buku</h1>
            <div className="nav-links">
              <Link to="/">Beranda</Link>
              <Link to="/stats">Statistik</Link>
            </div>
          </nav>
          
          <main className="main-content">
            {/* 3. Tentukan Rute Halaman */}
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/stats" element={<Stats />} />
            </Routes>
          </main>
        </div>
      </BrowserRouter>
    </BookProvider>
  );
}

export default App;