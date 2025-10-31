import React, { createContext, useContext, useState } from 'react';
import { useLocalStorage } from '../hooks/useLocalStorage';

// 1. Buat Context
const BookContext = createContext();

// 2. Buat custom hook untuk menggunakan context ini
export const useBooks = () => {
  return useContext(BookContext);
};

// 3. Buat Provider Component
export const BookProvider = ({ children }) => {
  const [books, setBooks] = useLocalStorage('books', []);
  const [filter, setFilter] = useState('all'); // 'all', 'milik', 'baca', 'beli'
  const [searchTerm, setSearchTerm] = useState('');

  const addBook = (book) => {
    const newBook = { ...book, id: Date.now() };
    setBooks(prevBooks => [...prevBooks, newBook]);
  };

  const updateBook = (id, updatedBook) => {
    setBooks(prevBooks =>
      prevBooks.map(book => (book.id === id ? { ...book, ...updatedBook } : book))
    );
  };

  const deleteBook = (id) => {
    setBooks(prevBooks => prevBooks.filter(book => book.id !== id));
  };

  // Nilai yang akan dibagikan ke semua komponen turunan
  const value = {
    books,
    addBook,
    updateBook,
    deleteBook,
    filter,
    setFilter,
    searchTerm,
    setSearchTerm,
  };

  return (
    <BookContext.Provider value={value}>
      {children}
    </BookContext.Provider>
  );
};