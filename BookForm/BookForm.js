import React, { useState, useEffect } from 'react';
import { useBooks } from '../../context/BookContext';
import './BookForm.css';

// Props:
// - bookToEdit: (object) Jika ada, form akan masuk mode edit
// - onComplete: (function) Fungsi untuk dipanggil setelah submit berhasil (untuk menutup/reset form)
const BookForm = ({ bookToEdit, onComplete }) => {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [status, setStatus] = useState('milik'); // default status
  const [error, setError] = useState('');
  const { addBook, updateBook } = useBooks();

  const isEditMode = !!bookToEdit;

  // Efek ini mengisi form jika kita dalam mode edit
  useEffect(() => {
    if (isEditMode) {
      setTitle(bookToEdit.title);
      setAuthor(bookToEdit.author);
      setStatus(bookToEdit.status);
      setError('');
    } else {
      // Jika tidak, reset form (misalnya setelah selesai mengedit)
      resetForm();
    }
  }, [bookToEdit, isEditMode]);

  const resetForm = () => {
    setTitle('');
    setAuthor('');
    setStatus('milik');
    setError('');
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Error Handling
    if (!title.trim() || !author.trim()) {
      setError('Judul dan Penulis tidak boleh kosong.');
      return;
    }

    const bookData = { title, author, status };

    if (isEditMode) {
      updateBook(bookToEdit.id, bookData);
    } else {
      addBook(bookData);
    }

    resetForm();
    if (onComplete) {
      onComplete(); // Panggil callback
    }
  };

  return (
    <form onSubmit={handleSubmit} className="book-form">
      {error && <p className="form-error">{error}</p>}
      <div className="form-group">
        <label htmlFor="title">Judul Buku</label>
        <input
          id="title"
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Mis: Laskar Pelangi"
        />
      </div>
      <div className="form-group">
        <label htmlFor="author">Penulis</label>
        <input
          id="author"
          type="text"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          placeholder="Mis: Andrea Hirata"
        />
      </div>
      <div className="form-group">
        <label htmlFor="status">Status</label>
        <select id="status" value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="milik">Sudah Dimiliki</option>
          <option value="baca">Sedang Dibaca</option>
          <option value="beli">Ingin Dibeli</option>
        </select>
      </div>
      <button type="submit" className="submit-btn">
        {isEditMode ? 'Update Buku' : 'Simpan Buku'}
      </button>
    </form>
  );
};

export default BookForm;