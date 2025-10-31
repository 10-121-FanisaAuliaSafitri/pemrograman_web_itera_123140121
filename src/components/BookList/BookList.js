import React, { useMemo } from 'react';
import { useBooks } from '../../context/BookContext';
import './BookList.css';

// Props:
// - onEdit: (function) Memberitahu parent (HomePage) buku mana yang akan diedit
const BookList = ({ onEdit }) => {
  const { books, deleteBook, filter, searchTerm } = useBooks();

  // Gunakan useMemo untuk performa.
  // Daftar ini hanya akan dihitung ulang jika dependensinya berubah.
  const filteredBooks = useMemo(() => {
    return books
      .filter(book => {
        // Filter berdasarkan status
        if (filter === 'all') return true;
        return book.status === filter;
      })
      .filter(book => {
        // Filter berdasarkan pencarian (judul atau penulis)
        const search = searchTerm.toLowerCase();
        return (
          book.title.toLowerCase().includes(search) ||
          book.author.toLowerCase().includes(search)
        );
      });
  }, [books, filter, searchTerm]);

  if (filteredBooks.length === 0) {
    return <p>Tidak ada buku yang ditemukan. Coba tambahkan buku baru!</p>;
  }

  return (
    <div className="book-list">
      {filteredBooks.map(book => (
        <div key={book.id} className="book-item">
          <div className="book-details">
            <h3 className="book-title">{book.title}</h3>
            <p className="book-author">oleh {book.author}</p>
          </div>
          <div className="book-meta">
            <span className={`book-status status-${book.status}`}>
              {book.status === 'milik' && 'Dimiliki'}
              {book.status === 'baca' && 'Dibaca'}
              {book.status === 'beli' && 'Ingin Dibeli'}
            </span>
            <div className="book-actions">
              <button onClick={() => onEdit(book)} className="btn-edit">
                Edit
              </button>
              <button onClick={() => deleteBook(book.id)} className="btn-delete">
                Hapus
              </button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default BookList;