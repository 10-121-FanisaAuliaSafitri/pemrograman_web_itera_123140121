import React from 'react';
import { useBooks } from '../../context/BookContext';
import { useBookStats } from '../../hooks/useBookStats';
import './Stats.css';

const Stats = () => {
  const { books } = useBooks(); // Ambil data buku dari context
  const stats = useBookStats(books); // Hitung statistik menggunakan custom hook

  return (
    <div className="stats-page">
      <h2>Statistik Buku</h2>
      <div className="stats-container">
        <div className="stat-card">
          <h4>Total Buku</h4>
          <p>{stats.total}</p>
        </div>
        <div className="stat-card">
          <h4>Sudah Dimiliki</h4>
          <p>{stats.owned}</p>
        </div>
        <div className="stat-card">
          <h4>Sedang Dibaca</h4>
          <p>{stats.reading}</p>
        </div>
        <div className="stat-card">
          <h4>Ingin Dibeli</h4>
          <p>{stats.toBuy}</p>
        </div>
      </div>
    </div>
  );
};

export default Stats;