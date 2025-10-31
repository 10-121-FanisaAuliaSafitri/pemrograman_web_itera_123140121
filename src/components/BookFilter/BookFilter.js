import React from 'react';
import { useBooks } from '../../context/BookContext';
import './BookFilter.css';

const BookFilter = () => {
  const { filter, setFilter, searchTerm, setSearchTerm } = useBooks();

  return (
    <div className="filter-container">
      <input
        type="text"
        className="search-input"
        placeholder="Cari buku berdasarkan judul atau penulis..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <div className="filter-buttons">
        <button
          className={filter === 'all' ? 'active' : ''}
          onClick={() => setFilter('all')}
        >
          Semua
        </button>
        <button
          className={filter === 'milik' ? 'active' : ''}
          onClick={() => setFilter('milik')}
        >
          Dimiliki
        </button>
        <button
          className={filter === 'baca' ? 'active' : ''}
          onClick={() => setFilter('baca')}
        >
          Dibaca
        </button>
        <button
          className={filter === 'beli' ? 'active' : ''}
          onClick={() => setFilter('beli')}
        >
          Ingin Dibeli
        </button>
      </div>
    </div>
  );
};

export default BookFilter;