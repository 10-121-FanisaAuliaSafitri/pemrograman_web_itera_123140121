import React, { useState } from 'react';
import BookForm from '../../components/BookForm/BookForm';
import BookFilter from '../../components/BookFilter/BookFilter';
import BookList from '../../components/BookList/BookList';

const Home = () => {
  // State lokal untuk melacak buku mana yang sedang diedit
  const [editingBook, setEditingBook] = useState(null);

  // Fungsi ini akan dipass ke BookList
  const handleEdit = (book) => {
    setEditingBook(book);
    window.scrollTo(0, 0); // Scroll ke atas untuk melihat form
  };

  // Fungsi ini akan dipass ke BookForm
  const handleComplete = () => {
    setEditingBook(null); // Selesai mengedit/menambah, reset form
  };

  return (
    <div className="home-page">
      <h2>{editingBook ? 'Edit Buku' : 'Tambah Buku Baru'}</h2>
      <BookForm bookToEdit={editingBook} onComplete={handleComplete} />

      <hr className="divider" />

      <h2>Daftar Buku Saya</h2>
      <BookFilter />
      <BookList onEdit={handleEdit} />
    </div>
  );
};

export default Home;